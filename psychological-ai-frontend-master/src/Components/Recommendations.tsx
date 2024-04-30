import axios from "axios";
import React, { useEffect, useState } from "react";
import { baseUrl } from "./Common/Constants";

function Recommendations({ recon }: any) {
  const [recoms, setRecoms] = useState<any>();

  useEffect(() => {
    getRecoms();
    console.log("reconss", recon);
  }, [recon]);

  const getRecoms = async () => {
    const res = await axios.post(baseUrl + "vtov/getRecommendations/", recon);

    setRecoms(res.data);
    console.log("recoms", res.data);
  };

  return (
    <>
      {recon && (
        <>
          <div className="card text-center shadow-2xl mt-20">
            <div className="card-body">
              <h2 className="card-title text-3xl">Recommendations</h2>
              <div className="divider" style={{ marginTop: "0rem" }}></div>
              <ol>
                {Object.entries(recoms).map((key, val) => {
                  return (
                    <li className="my-10 p-5 border border-indigo-400 rounded-2xl">
                      {/* {console.log(key[1], "hereeeeeeeeeeeeeeee")} */}
                      {key[1]}
                      {val}
                    </li>
                  );
                })}
              </ol>
              <div className="justify-center card-actions">
                <button className="btn btn-outline btn-accent">
                  More info
                </button>
              </div>
            </div>
          </div>
        </>
      )}

      {/* <div className="mt-4" id="whoobe-avqbm">
            Your Email
          </div> */}
      {/* <input
            type="email"
            value=""
            className="p-1 w-full border-gray-200"
            id="email"
            name="email"
            placeholder="your email is required"
          /> */}
      {/* <button
            type="button"
            value="button"
            className="hover:text-white hover:bg-green-400 bg-gray-800 text-gray-400 m-auto my-4 px-6 py-2 text-lg rounded shadow-px-4 border-0"
            id="whoobe-wkfvm"
          >
            Subscribe
          </button> */}
    </>
  );
}

export default Recommendations;
