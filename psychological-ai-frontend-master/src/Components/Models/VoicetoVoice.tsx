import axios from "axios";
import React, { useEffect, useState } from "react";
import { baseUrl } from "../Common/Constants";
import Spinner from "../Widgets/Spinner";

function VoicetoVoice({ setRecon }: any) {
  const [tests, setTests] = useState<string>("");
  const [diag, setDiag] = useState();
  const [severity, setSeverity] = useState({});

  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // classify().then(async () => {
    // await diagnosis();
    // });
  }, []);

  const classify = async () => {
    const res = await axios.get(baseUrl + "vtov/");

    setTests(res.data);
    console.log("i got the result", res.data);
  };

  const diagnosis = async () => {
    const res = await axios.post(baseUrl + "vtov/diagnose/", tests);

    console.log(res);
    setDiag(res.data);
    console.log("i got the diagnosis", res.data);

    if (res.data) {
      const t = saveHistory(res.data);
      console.log(t, "savedddddddddddddddddd");
    }
  };

  const saveHistory = async (data: any) => {
    setLoading(true);
    const res = await axios.post(baseUrl + "vtov/saveHistory/", data);

    return res;
  };

  const getSeverity = async () => {
    const res = await axios.post(baseUrl + "vtov/getSeverity/", diag);

    setSeverity(res.data);
    setRecon(res.data);
    console.log("i got the severity", res.data);
    setLoading(false);
  };

  return (
    <div className="relative flex flex-col justify-between p-8 lg:p-6 xl:p-8 rounded-2xl md:col-span-2 lg:col-span-1">
      <div className="absolute inset-0 w-full h-full transform translate-x-2 translate-y-2 bg-red-50 rounded-2xl"></div>
      <div className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-2xl"></div>
      <div className="relative flex pb-5 space-x-5 border-b border-gray-200 lg:space-x-3 xl:space-x-5">
        {/* <svg
                className="w-16 h-16 text-red-400 rounded-2xl"
                viewBox="0 0 150 150"
                xmlns="http://www.w3.org/2000/svg"
              >
                <defs>
                  <rect x="0" y="0" width="150" height="150" rx="15"></rect>
                </defs>
                <g fill="none" fill-rule="evenodd">
                  <mask fill="#fff">
                    <use></use>
                  </mask>
                  <use fill="currentColor"></use>
                  <circle
                    fill-opacity=".3"
                    fill="#FFF"
                    mask="url(#plan1)"
                    cx="125"
                    cy="25"
                    r="50"
                  ></circle>
                  <path
                    fill-opacity=".3"
                    fill="#FFF"
                    mask="url(#plan1)"
                    d="M-33 83H67v100H-33z"
                  ></path>
                </g>
              </svg> */}

        <div className="relative flex flex-col items-start">
          <h3 className="text-xl font-bold ml-20">Voice to Voice</h3>
          <img
            className=" rounded-lg"
            src="https://image.freepik.com/free-vector/funny-young-woman-screaming-megaphone_73637-662.jpg"
          />
          <p className="tracking-tight text-gray-500">
            {/* <span className="text-sm transform inline-block -translate-y-2.5 relative">
                    $
                  </span>
                  <span className="text-3xl font-bold text-gray-800">35</span>
                  <span className="text-sm -translate-y-0.5 inline-block transform">
                    / user
                  </span> */}
          </p>
        </div>
      </div>

      <ul className="relative py-12 space-y-3">
        {Object.entries(severity).map((key, index) => {
          return (
            <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
              <svg
                className="w-6 h-6 text-red-400"
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
              <span>
                {key[0]} : {key[1]}
              </span>
            </li>
          );
        })}

        {loading && <Spinner />}

        {/* <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
                <svg
                  className="w-6 h-6 text-red-400"
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
                <span>Custom Design &amp; Features</span>
              </li> */}
        {/* <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
                <svg
                  className="w-6 h-6 text-red-400"
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
                <span>Access to 500+ Components</span>
              </li>
              <li className="flex items-center space-x-2 text-sm font-medium text-gray-500">
                <svg
                  className="w-6 h-6 text-red-400"
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
                <span>Priority Phone Support</span>
              </li> */}
      </ul>

      <div
        onClick={() => {
          classify();
        }}
        className="relative flex items-center justify-center w-full px-5 py-5 text-lg font-medium text-white rounded-xl group my-2"
      >
        <span className="w-full h-full absolute inset-0 transform translate-y-1.5 translate-x-1.5 group-hover:translate-y-0 group-hover:translate-x-0 transition-all ease-out duration-200 rounded-xl bg-red-400"></span>
        <span className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-xl"></span>
        <span className="relative">Start Counselling</span>
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
      <div
        onClick={() => {
          diagnosis();
        }}
        className="relative flex items-center justify-center w-full px-5 py-5 text-lg font-medium text-white rounded-xl group my-2"
      >
        <span className="w-full h-full absolute inset-0 transform translate-y-1.5 translate-x-1.5 group-hover:translate-y-0 group-hover:translate-x-0 transition-all ease-out duration-200 rounded-xl bg-red-400"></span>
        <span className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-xl"></span>
        <span className="relative">Start Diagnosis</span>
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
      <div
        onClick={() => {
          getSeverity();
        }}
        className="relative flex items-center justify-center w-full px-5 py-5 text-lg font-medium text-white rounded-xl group my-2"
      >
        <span className="w-full h-full absolute inset-0 transform translate-y-1.5 translate-x-1.5 group-hover:translate-y-0 group-hover:translate-x-0 transition-all ease-out duration-200 rounded-xl bg-red-400"></span>
        <span className="absolute inset-0 w-full h-full border-2 border-gray-900 rounded-xl"></span>
        <span className="relative">Get Severity</span>
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

export default VoicetoVoice;
