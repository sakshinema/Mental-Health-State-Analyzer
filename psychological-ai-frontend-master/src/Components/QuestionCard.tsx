import React, { useEffect, useState } from "react";

interface QuesCard {
  onChange: (...event: any[]) => void;

  quesData: [string, string[][]];
}

const QuestionCard = ({ onChange, quesData }: QuesCard) => {
  return (
    <div className="m-10 p-6 card bordered" style={{ borderColor: "black" }}>
      {quesData[1].map((option) => {
        return (
          <div className="form-control">
            <label className="cursor-pointer label">
              <span className="label-text">{option[0]}</span>
              <input
                type="radio"
                name="opt"
                className="radio radio-accent"
                value={option[1]}
                onChange={(value) => {
                  onChange(value.target.value);
                }}
              />
            </label>
          </div>
        );
      })}
      {/* 
      <div className="form-control">
        <label className="cursor-pointer label">
          <span className="label-text">Neutral</span>
          <input type="radio" name="opt" className="radio" value="" />
        </label>
      </div>
      <div className="form-control">
        <label className="cursor-pointer label">
          <span className="label-text">Primary</span>
          <input
            type="radio"
            name="opt"
            className="radio radio-primary"
            value=""
          />
        </label>
      </div>
      <div className="form-control">
        <label className="cursor-pointer label">
          <span className="label-text">Secondary</span>
          <input
            type="radio"
            name="opt"
            className="radio radio-secondary"
            value=""
          />
        </label>
      </div>
      <div className="form-control">
        <label className="cursor-pointer label">
          <span className="label-text">Accent</span>
          <input
            type="radio"
            name="opt"
            className="radio radio-accent"
            value=""
          />
        </label>
      </div>
      <div className="form-control">
        <label className="label">
          <span className="label-text">Disabled</span>
          <input type="radio" name="opt" value="" className="radio" />
        </label>
      </div> */}
    </div>
  );
};

export default QuestionCard;
