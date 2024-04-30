import axios from "axios";
import React, { useEffect, useState } from "react";
import Navbar from "./Navbar";
import { baseUrl } from "./Common/Constants";

function History() {
  const [history, setHistory] = useState<any>();

  useEffect(() => {
    getHistory();
  }, []);

  const getHistory = async () => {
    const res = await axios.get(baseUrl + "vtov/getHistory/");

    setHistory(res.data);
    console.log("history", res.data);
  };

  return (
    <>
      <Navbar />

      <div className="py-10 mx-48">
        <div className="card text-center shadow-2xl">
          <div className="card-body">
            <h2 className="card-title text-3xl">History</h2>
            <hr />
            {history && (
              <ul>
                {console.log("hissssss", history)}
                {Object.entries(history.rahul).map((key, index) => {
                  return (
                    <li className="my-10 border border-indigo-400 rounded-2xl">
                      {console.log(key[1])}
                      {key[0].toString().split(" ")[0]}
                      <br />
                      {key[0].toString().split(" ")[1]}
                      <br />
                      {Object.entries(key[1]).map((key) => {
                        return (
                          <>
                            {key[0]} ~ {key[1]}
                            <br />
                          </>
                        );
                      })}
                    </li>
                  );
                })}
              </ul>
            )}
            {/* <div className="justify-center card-actions">
              <button className="btn btn-outline btn-accent">More info</button>
            </div> */}
          </div>
        </div>
      </div>
    </>
  );
}

export default History;
