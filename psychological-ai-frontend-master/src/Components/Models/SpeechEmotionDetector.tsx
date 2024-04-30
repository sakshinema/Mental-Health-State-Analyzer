import axios from "axios";
import React, { useEffect, useState } from "react";
import { baseUrl } from "../Common/Constants";
import Spinner from "../Widgets/Spinner";

function SpeechEmotionDetector({ overallScore, setOverallScore }: any) {
  const [emotion, setEmotion] = useState<any>();
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // getEmotion();
  }, []);

  const getEmotion = async () => {
    setLoading(true);
    const res = await axios.get(baseUrl + "speech_emotion/");

    console.log(res.data, "speech emotion");
    setEmotion(res.data);
    setOverallScore({ ...overallScore, speechArr: res.data });
    setLoading(false);
  };

  return (
    <div className="relative flex flex-col justify-between p-8 lg:p-6 xl:p-8 rounded-2xl">
      <div className="absolute inset-0 w-full h-full transform translate-x-2 translate-y-2 bg-green-50 rounded-2xl"></div>
      <div className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-2xl"></div>
      <div className="relative flex pb-5 space-x-5 border-b border-gray-200 lg:space-x-3 xl:space-x-5">
        <div className="relative flex flex-col">
          <h3 className="text-xl font-bold ml-10">Speech Emotion Detector</h3>
          <img
            className=" rounded-lg"
            src="https://image.freepik.com/free-vector/old-man-sitting-park-chair-reading-book-relaxed-with-his-dog-hand-drawing-vector-illustration-doodle-style_73637-638.jpg"
          />
          {/* <p className="tracking-tight text-gray-500">
            <span className="text-sm transform inline-block -translate-y-2.5 relative">
              $
            </span>
            <span className="text-3xl font-bold text-gray-800">10</span>
            <span className="text-sm -translate-y-0.5 inline-block transform">
              / user
            </span>
          </p> */}
        </div>
      </div>

      {loading && <Spinner />}

      {emotion && (
        <ul className="relative py-12 space-y-3">
          {emotion.Emotion.map((emo: any) => (
            <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
              <svg
                className="w-6 h-6 text-green-400"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              <span>{emo}</span>
            </li>
          ))}

          {/* <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
          <svg
            className="w-6 h-6 text-green-400"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span>2</span>
        </li>
        <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
          <svg
            className="w-6 h-6 text-green-400"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span>3</span>
        </li> */}
        </ul>
      )}

      <div
        onClick={() => {
          getEmotion();
        }}
        className="relative flex items-center justify-center w-full px-5 py-5 text-lg font-medium text-white rounded-xl group"
      >
        <span className="w-full h-full absolute inset-0 transform translate-y-1.5 translate-x-1.5 group-hover:translate-y-0 group-hover:translate-x-0 transition-all ease-out duration-200 rounded-xl bg-green-500"></span>
        <span className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-xl"></span>
        <span className="relative">Get Emotion</span>
        <svg
          className="w-5 h-5 ml-2 transition-all duration-200 ease-out transform group-hover:translate-x-1"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </div>
    </div>
  );
}

export default SpeechEmotionDetector;
