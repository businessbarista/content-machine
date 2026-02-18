import React from "react";
import { AbsoluteFill } from "remotion";
import {
  TransitionSeries,
  linearTiming,
} from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { CaptionedClip } from "./CaptionedClip";
import { IntroOutro } from "./IntroOutro";

interface FullEditProps {
  videoSrc: string;
  captionsSrc: string;
  highlightColor: string;
  showIntro: boolean;
  showOutro: boolean;
  introTitle: string;
  outroText: string;
  logoSrc: string;
  brandColor: string;
  backgroundColor: string;
}

export const FullEdit: React.FC<FullEditProps> = ({
  videoSrc,
  captionsSrc,
  highlightColor,
  showIntro,
  showOutro,
  introTitle,
  outroText,
  logoSrc,
  brandColor,
  backgroundColor,
}) => {
  const introFrames = 90; // 3 seconds at 30fps
  const outroFrames = 90;
  const transitionFrames = 15;
  // Main content fills remaining frames
  const mainFrames = 1800 - (showIntro ? introFrames : 0) - (showOutro ? outroFrames : 0);

  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      <TransitionSeries>
        {showIntro && (
          <>
            <TransitionSeries.Sequence durationInFrames={introFrames}>
              <IntroOutro
                type="intro"
                title={introTitle}
                logoSrc={logoSrc}
                brandColor={brandColor}
                backgroundColor={backgroundColor}
              />
            </TransitionSeries.Sequence>
            <TransitionSeries.Transition
              presentation={fade()}
              timing={linearTiming({ durationInFrames: transitionFrames })}
            />
          </>
        )}

        <TransitionSeries.Sequence durationInFrames={mainFrames}>
          <CaptionedClip
            videoSrc={videoSrc}
            captionsSrc={captionsSrc}
            highlightColor={highlightColor}
            fontFamily="Inter"
            fontSize={70}
          />
        </TransitionSeries.Sequence>

        {showOutro && (
          <>
            <TransitionSeries.Transition
              presentation={fade()}
              timing={linearTiming({ durationInFrames: transitionFrames })}
            />
            <TransitionSeries.Sequence durationInFrames={outroFrames}>
              <IntroOutro
                type="outro"
                title={outroText || "Thanks for watching"}
                logoSrc={logoSrc}
                brandColor={brandColor}
                backgroundColor={backgroundColor}
              />
            </TransitionSeries.Sequence>
          </>
        )}
      </TransitionSeries>
    </AbsoluteFill>
  );
};
