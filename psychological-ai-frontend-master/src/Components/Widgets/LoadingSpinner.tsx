const LoadingSpinner = () => {
  return (
    <>
      <div className={"h-screen flex items-center justify-center"}>
        <div className="loader ease-linear rounded-full border-8 border-t-8 border-gray-200 h-64 w-64"></div>
      </div>
    </>
  );
};

export default LoadingSpinner;
