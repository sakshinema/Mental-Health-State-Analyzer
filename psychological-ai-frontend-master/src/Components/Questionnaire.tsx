import React, { useEffect, useState } from "react";
import { Controller, useForm } from "react-hook-form";

import { adhd } from "./Data/adhd";
import QuestionCard from "./QuestionCard";

function Questionnaire() {
  const { control, handleSubmit, register, watch } = useForm();
  const [questions, setQuestions] = useState<any>([]);
  console.log(watch());
  return (
    <>
      <div>
        {adhd.map((quesData, index) => {
          // console.log(quesData);
          return (
            <>
              <div className="m-10 p-2">{quesData[0]}</div>
              <Controller
                control={control} 
                name={index.toString()}
                render={({ field: { onChange, value } }) => (
                  <QuestionCard onChange={onChange} quesData={quesData} />
                )}
              />
            </>
          );
        })}
      </div>
    </>
  );
}

export default Questionnaire;
