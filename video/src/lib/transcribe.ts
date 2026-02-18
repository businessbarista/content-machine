import path from "path";
import fs from "fs";
import {
  downloadWhisperModel,
  installWhisperCpp,
  transcribe,
  toCaptions,
} from "@remotion/install-whisper-cpp";

const WHISPER_VERSION = "1.5.5";
const MODEL = "medium.en";

async function main() {
  const inputPath = process.argv[2];
  const outputPath = process.argv[3] || "captions.json";

  if (!inputPath) {
    console.error("Usage: npx tsx src/lib/transcribe.ts <audio.wav> [output.json]");
    console.error("");
    console.error("The input audio must be a 16KHz WAV file.");
    console.error("Convert from video: ffmpeg -i input.mp4 -ar 16000 -ac 1 audio.wav");
    process.exit(1);
  }

  if (!fs.existsSync(inputPath)) {
    console.error(`File not found: ${inputPath}`);
    process.exit(1);
  }

  const whisperPath = path.join(process.cwd(), "whisper.cpp");

  // Install Whisper.cpp if not already installed
  if (!fs.existsSync(whisperPath)) {
    console.log("Installing Whisper.cpp...");
    await installWhisperCpp({
      to: whisperPath,
      version: WHISPER_VERSION,
    });
  }

  // Download model if not already downloaded
  const modelPath = path.join(whisperPath, `ggml-${MODEL}.bin`);
  if (!fs.existsSync(modelPath)) {
    console.log(`Downloading Whisper model: ${MODEL}...`);
    await downloadWhisperModel({
      model: MODEL,
      folder: whisperPath,
    });
  }

  console.log("Transcribing...");
  const whisperOutput = await transcribe({
    model: MODEL,
    whisperPath,
    whisperCppVersion: WHISPER_VERSION,
    inputPath: path.resolve(inputPath),
    tokenLevelTimestamps: true,
  });

  const { captions } = toCaptions({ whisperCppOutput: whisperOutput });

  // Save to JSON (Remotion Caption format)
  fs.writeFileSync(outputPath, JSON.stringify(captions, null, 2));
  console.log(`Captions saved to: ${outputPath}`);
  console.log(`Total captions: ${captions.length}`);

  // Also save a readable text version
  const textPath = outputPath.replace(".json", ".md");
  const textContent = captions.map((c) => c.text).join(" ");
  fs.writeFileSync(textPath, `# Transcript\n\n${textContent}\n`);
  console.log(`Readable transcript saved to: ${textPath}`);
}

main().catch((err) => {
  console.error("Transcription failed:", err);
  process.exit(1);
});
