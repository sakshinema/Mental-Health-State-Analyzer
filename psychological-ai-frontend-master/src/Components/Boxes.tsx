import React, { useState } from "react";
import EmotionDetector from "./Models/EmotionDetector";
import SpeechEmotionDetector from "./Models/SpeechEmotionDetector";
import VoicetoVoice from "./Models/VoicetoVoice";
import OverallScore from "./OverallScore";
import Recommendations from "./Recommendations";

function Boxes() {
  const [recon, setRecon] = useState();

  interface IOverallScore {
    faceArr: any[];
    speechArr: any[];
    quest: string;
  }

  const [overallScore, setOverallScore] = useState<IOverallScore>();

  return (
    <section className="w-full pt-16 pb-20 bg-gray-50">
      <div className="px-10 mx-auto text-center max-w-7xl">
        <h2 className="text-5xl font-bold text-blue-600">
          Mental Health <span className="text-gray-800">Status Analyzer</span>
        </h2>
        <progress
          className="progress progress-error"
          value="100"
          max="100"
        ></progress>
        {/* <p className="mt-3 text-lg text-gray-500">something like a tagline</p> */}
        <div className="grid gap-5 mt-12 lg:grid-cols-3 md:grid-cols-2">
          <EmotionDetector
            overallScore={overallScore}
            setOverallScore={setOverallScore}
          />

          <VoicetoVoice setRecon={setRecon} />

          <SpeechEmotionDetector
            overallScore={overallScore}
            setOverallScore={setOverallScore}
          />
        </div>
        <Recommendations recon={recon} />
        <OverallScore score={overallScore} />
      </div>
    </section>
  );
}

export default Boxes;
