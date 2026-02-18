import React from "react";
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  staticFile,
  Img,
} from "remotion";

interface IntroOutroProps {
  type: "intro" | "outro";
  title: string;
  subtitle?: string;
  logoSrc?: string;
  brandColor: string;
  backgroundColor: string;
}

export const IntroOutro: React.FC<IntroOutroProps> = ({
  type,
  title,
  subtitle,
  logoSrc,
  brandColor,
  backgroundColor,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const isIntro = type === "intro";

  // Fade in at start
  const fadeIn = interpolate(frame, [0, 0.5 * fps], [0, 1], {
    extrapolateRight: "clamp",
  });

  // Fade out at end
  const fadeOut = interpolate(
    frame,
    [durationInFrames - 0.5 * fps, durationInFrames],
    [1, 0],
    { extrapolateLeft: "clamp" }
  );

  const opacity = Math.min(fadeIn, fadeOut);

  // Scale animation for logo
  const logoScale = interpolate(frame, [0, 0.8 * fps], [0.8, 1], {
    extrapolateRight: "clamp",
  });

  // Title slide up
  const titleY = interpolate(frame, [0.2 * fps, 0.7 * fps], [30, 0], {
    extrapolateRight: "clamp",
    extrapolateLeft: "clamp",
  });

  const titleOpacity = interpolate(frame, [0.2 * fps, 0.7 * fps], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor,
        justifyContent: "center",
        alignItems: "center",
        opacity,
      }}
    >
      {logoSrc && (
        <Img
          src={staticFile(logoSrc)}
          style={{
            width: 120,
            height: 120,
            objectFit: "contain",
            transform: `scale(${logoScale})`,
            marginBottom: 24,
          }}
        />
      )}
      <div
        style={{
          transform: `translateY(${titleY}px)`,
          opacity: titleOpacity,
          textAlign: "center",
          padding: "0 10%",
        }}
      >
        <div
          style={{
            color: brandColor,
            fontSize: 52,
            fontWeight: "bold",
            lineHeight: 1.2,
          }}
        >
          {title}
        </div>
        {subtitle && (
          <div
            style={{
              color: "rgba(255,255,255,0.7)",
              fontSize: 28,
              marginTop: 12,
            }}
          >
            {subtitle}
          </div>
        )}
      </div>
      {!isIntro && (
        <div
          style={{
            position: "absolute",
            bottom: "12%",
            color: "rgba(255,255,255,0.5)",
            fontSize: 20,
          }}
        >
          {subtitle || ""}
        </div>
      )}
    </AbsoluteFill>
  );
};
