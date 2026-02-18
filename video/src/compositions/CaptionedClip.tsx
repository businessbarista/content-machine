import React from "react";
import { AbsoluteFill, staticFile } from "remotion";
import { Video } from "@remotion/media";
import { Captions } from "../components/Captions";

interface CaptionedClipProps {
  videoSrc: string;
  captionsSrc: string;
  highlightColor: string;
  fontFamily: string;
  fontSize: number;
}

export const CaptionedClip: React.FC<CaptionedClipProps> = ({
  videoSrc,
  captionsSrc,
  highlightColor,
  fontFamily,
  fontSize,
}) => {
  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      <Video
        src={staticFile(videoSrc)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
        }}
      />
      <Captions
        captionsSrc={captionsSrc}
        highlightColor={highlightColor}
        fontFamily={fontFamily}
        fontSize={fontSize}
      />
    </AbsoluteFill>
  );
};
