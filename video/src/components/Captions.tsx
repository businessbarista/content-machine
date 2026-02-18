import React, { useState, useCallback, useMemo } from "react";
import {
  AbsoluteFill,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  Sequence,
  continueRender,
  cancelRender,
  delayRender,
} from "remotion";
import type { Caption, TikTokPage } from "@remotion/captions";
import { createTikTokStyleCaptions } from "@remotion/captions";

interface CaptionsProps {
  captionsSrc: string;
  highlightColor: string;
  fontFamily: string;
  fontSize: number;
}

const SWITCH_CAPTIONS_EVERY_MS = 1200;

const CaptionPage: React.FC<{
  page: TikTokPage;
  highlightColor: string;
  fontFamily: string;
  fontSize: number;
}> = ({ page, highlightColor, fontFamily, fontSize }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTimeMs = (frame / fps) * 1000;
  const absoluteTimeMs = page.startMs + currentTimeMs;

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "center",
        paddingBottom: "15%",
      }}
    >
      <div
        style={{
          fontSize,
          fontWeight: "bold",
          fontFamily,
          textAlign: "center",
          textShadow: "0 2px 8px rgba(0,0,0,0.8)",
          maxWidth: "90%",
          lineHeight: 1.2,
        }}
      >
        {page.tokens.map((token) => {
          const isActive =
            token.fromMs <= absoluteTimeMs && token.toMs > absoluteTimeMs;
          return (
            <span
              key={token.fromMs}
              style={{
                color: isActive ? highlightColor : "white",
                transition: "none",
              }}
            >
              {token.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

export const Captions: React.FC<CaptionsProps> = ({
  captionsSrc,
  highlightColor,
  fontFamily,
  fontSize,
}) => {
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const [handle] = useState(() => delayRender("Loading captions"));
  const { fps } = useVideoConfig();

  const fetchCaptions = useCallback(async () => {
    try {
      const response = await fetch(staticFile(captionsSrc));
      const data = await response.json();
      setCaptions(data);
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [captionsSrc, continueRender, cancelRender, handle]);

  React.useEffect(() => {
    fetchCaptions();
  }, [fetchCaptions]);

  const pages = useMemo(() => {
    if (!captions) return [];
    const { pages } = createTikTokStyleCaptions({
      captions,
      combineTokensWithinMilliseconds: SWITCH_CAPTIONS_EVERY_MS,
    });
    return pages;
  }, [captions]);

  if (!captions) return null;

  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        const nextPage = pages[index + 1] ?? null;
        const startFrame = (page.startMs / 1000) * fps;
        const endFrame = Math.min(
          nextPage ? (nextPage.startMs / 1000) * fps : Infinity,
          startFrame + (SWITCH_CAPTIONS_EVERY_MS / 1000) * fps
        );
        const durationInFrames = endFrame - startFrame;

        if (durationInFrames <= 0) return null;

        return (
          <Sequence
            key={index}
            from={Math.round(startFrame)}
            durationInFrames={Math.round(durationInFrames)}
          >
            <CaptionPage
              page={page}
              highlightColor={highlightColor}
              fontFamily={fontFamily}
              fontSize={fontSize}
            />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
