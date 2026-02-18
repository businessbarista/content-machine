import { Composition, Folder } from "remotion";
import { CaptionedClip } from "./compositions/CaptionedClip";
import { IntroOutro } from "./compositions/IntroOutro";
import { FullEdit } from "./compositions/FullEdit";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Folder name="Content Machine">
        <Composition
          id="CaptionedClip"
          component={CaptionedClip}
          durationInFrames={900}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            videoSrc: "video.mp4",
            captionsSrc: "captions.json",
            highlightColor: "#39E508",
            fontFamily: "Inter",
            fontSize: 70,
          }}
        />
        <Composition
          id="IntroOutro"
          component={IntroOutro}
          durationInFrames={150}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            type: "intro" as const,
            title: "Human in the Loop",
            subtitle: "",
            logoSrc: "",
            brandColor: "#ffffff",
            backgroundColor: "#000000",
          }}
        />
        <Composition
          id="FullEdit"
          component={FullEdit}
          durationInFrames={1800}
          fps={30}
          width={1080}
          height={1920}
          defaultProps={{
            videoSrc: "video.mp4",
            captionsSrc: "captions.json",
            highlightColor: "#39E508",
            showIntro: true,
            showOutro: true,
            introTitle: "",
            outroText: "",
            logoSrc: "",
            brandColor: "#ffffff",
            backgroundColor: "#000000",
          }}
        />
      </Folder>
    </>
  );
};
