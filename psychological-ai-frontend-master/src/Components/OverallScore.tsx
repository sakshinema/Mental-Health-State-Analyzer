import axios from "axios";
import React, { useEffect, useState } from "react";
import { baseUrl } from "./Common/Constants";

function OverallScore({ score }: any) {
  const [theScore, setTheScore] = useState<any>();

  const getScore = async () => {
    const res = await axios.post(baseUrl + "vtov/getOverallScore/", score);
    console.log("scoressss", res.data);
    setTheScore(res.data);
  };

  useEffect(() => {
    const res = getScore();

    console.log(res);
  }, []);

  return (
    <div className="card text-center shadow-2xl mt-20">
      <div className="card-body">
        <>
          <h2 className="card-title text-3xl">Overall Score</h2>
          <button
            className="btn btn-error"
            onClick={() => {
              getScore();
            }}
          >
            Get Overall Score
          </button>
          {theScore && (
            <>
              <div className="divider" style={{ marginTop: "0rem  " }}></div>
              <div className="w-full shadow stats">
                <div className="stat">
                  <div className="stat-figure text-primary">
                    {/* <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block w-8 h-8 stroke-current"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
                ></path>
              </svg> */}
                  </div>
                  <div className="stat-title">Score</div>
                  <div className="stat-value text-primary">
                    {theScore.score}
                  </div>
                  {/* <div className="stat-desc">21% more than last month</div> */}
                </div>
                <div className="stat">
                  <div className="stat-figure text-info">
                    {/* <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block w-8 h-8 stroke-current"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                ></path>
              </svg> */}
                  </div>
                  <div className="stat-title">Verdict</div>
                  <div className="stat-value text-info">
                    {theScore.verdict.toString().toUpperCase()}
                  </div>
                  {/* <div className="stat-desc">21% more than last month</div> */}
                </div>
              </div>
            </>
          )}
        </>
      </div>
    </div>
  );
}

export default OverallScore;
