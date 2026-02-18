import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from "remotion";

interface BrandLowerThirdProps {
  name: string;
  title?: string;
  brandColor: string;
  fontFamily?: string;
}

export const BrandLowerThird: React.FC<BrandLowerThirdProps> = ({
  name,
  title,
  brandColor,
  fontFamily = "Inter",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const slideIn = interpolate(frame, [0, 0.5 * fps], [100, 0], {
    extrapolateRight: "clamp",
  });

  const opacity = interpolate(frame, [0, 0.3 * fps], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        justifyContent: "flex-end",
        alignItems: "flex-start",
        padding: "8%",
        paddingBottom: "25%",
      }}
    >
      <div
        style={{
          transform: `translateX(${slideIn}px)`,
          opacity,
          fontFamily,
        }}
      >
        <div
          style={{
            backgroundColor: brandColor,
            color: "white",
            padding: "8px 16px",
            fontSize: 28,
            fontWeight: "bold",
            display: "inline-block",
          }}
        >
          {name}
        </div>
        {title && (
          <div
            style={{
              backgroundColor: "rgba(0,0,0,0.7)",
              color: "white",
              padding: "6px 16px",
              fontSize: 20,
              display: "inline-block",
              marginTop: 4,
            }}
          >
            {title}
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
