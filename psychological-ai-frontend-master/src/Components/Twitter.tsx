import axios from "axios";
import React, { useEffect, useState } from "react";
import { baseUrl } from "./Common/Constants";
import Navbar from "./Navbar";

function Twitter() {
  const [tweets, setTweets] = useState<{ count: number; data: any[] }>();
  const [username, setUsername] = useState("elonmusk");
  const [tweetCount, setTweetCount] = useState("10");

  useEffect(() => {
    getTweets();

    console.log(tweets);
  }, []);

  const getTweets = async () => {
    const res = await axios.post(baseUrl + "twitter/tweets/", {
      query: username,
      tweetCount: tweetCount,
    });

    console.log(res.data);
    setTweets(res.data);
    console.log(tweets);
  };

  return (
    <>
      <Navbar />

      <div className="py-10 mx-5">
        {/* Input */}
        <div className="form-control flex flex-row justify-center">
          <label className="input-group">
            <span> @ </span>
            <input
              type="text"
              placeholder="username"
              className="input input-bordered"
              onChange={(event) => {
                setUsername(event.target.value);
                // console.log(username);
              }}
            />
          </label>
          <label className="input-group ml-10">
            <span> No. of Tweets </span>
            <input
              type="text"
              placeholder="tweet count"
              className="input input-bordered"
              onChange={(event) => {
                setTweetCount(event.target.value);
                // console.log(tweetCount);
              }}
            />
          </label>
          <button
            className="btn btn-info ml-10"
            onClick={() => {
              getTweets();
            }}
          >
            Analyze
          </button>
        </div>

        {/* Tweets  */}
        <div className="py-10">
          <div className="overflow-x-auto">
            <table className="table w-full">
              <thead>
                <tr>
                  <th>
                    <label>
                      <input type="checkbox" className="checkbox" />
                    </label>
                  </th>
                  <th>Tweet</th>
                  <th>Sentiment</th>
                  <th>Sentiment Vader</th>
                  {/* <th></th> */}
                </tr>
              </thead>
              <tbody>
                {tweets &&
                  tweets.data.map((tweet) => (
                    <>
                      <tr>
                        <th>
                          <label>
                            <input type="checkbox" className="checkbox" />
                          </label>
                        </th>
                        <td>
                          <div className="flex items-center space-x-3">
                            {/* <div className="avatar">
                            <div className="w-12 h-12 mask mask-squircle">
                              <img
                                src="/tailwind-css-component-profile-2@56w.png"
                                alt="Avatar Tailwind CSS Component"
                              />{" "}
                            </div>
                          </div> */}
                            <div>
                              <div className="font-bold">
                                <p>{tweet.text}</p>
                              </div>
                              {/* <div className="text-sm opacity-50">
                              United States
                            </div> */}
                            </div>
                          </div>
                        </td>
                        <td>
                          {tweet.sentiment}
                          <br />
                          {/* <span className="badge badge-outline badge-sm">
                          Desktop Support Technician
                        </span> */}
                        </td>
                        <td>{tweet.sentiment_vader}</td>
                      </tr>
                    </>
                  ))}
              </tbody>
              <tfoot>
                <tr>
                  <th></th>
                  <th>Tweet</th>
                  <th>Sentiment</th>
                  <th>Sentiment Vader</th>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>
      </div>
    </>
  );
}

export default Twitter;
