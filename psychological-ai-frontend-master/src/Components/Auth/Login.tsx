import { useState } from "react";
import { useForm } from "react-hook-form";
import { useHistory, Link } from "react-router-dom";
import LoadingSpinner from "../Widgets/LoadingSpinner";
import { LoginHandler } from "./AuthService";
import { ILogin } from "../Common/Interfaces";

const Login = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  let history = useHistory();
  const [isLoading, setIsLoading] = useState(false);

  const onSubmit = async (data: ILogin) => {
    console.log(data);
    setIsLoading(true);

    const res = await LoginHandler(data);

    history.push("/");
  };

  return (
    <>
      {isLoading ? (
        <LoadingSpinner />
      ) : (
        <div className="h-screen w-full flex flex-col items-center justify-center sl">
          <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl sm:truncate">
            Login
          </h2>
          <div className="w-full max-w-xs">
            <form
              className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
              onSubmit={handleSubmit(onSubmit)}
            >
              <div className="mb-4">
                <label
                  className="block text-gray-700 text-sm font-bold mb-2"
                  htmlFor="username"
                >
                  Username
                </label>
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  id="username"
                  {...register("username", { required: true })}
                />
                {errors.username && (
                  <p className="text-red-500 text-xs italic">
                    Please choose a username.
                  </p>
                )}
              </div>
              <div className="mb-6">
                <label
                  className="block text-gray-700 text-sm font-bold mb-2"
                  htmlFor="password"
                >
                  Password
                </label>
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
                  id="password"
                  type="password"
                  placeholder="*******"
                  {...register("password", {
                    required: true,
                  })}
                />
                {errors.password && (
                  <p className="text-red-500 text-xs italic">
                    Please choose a password.
                  </p>
                )}
              </div>
              <div className="flex items-center justify-between">
                <button
                  className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  type="submit"
                >
                  Sign In
                </button>
                <Link
                  to={"/register"}
                  className="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
                >
                  New User?
                </Link>
              </div>
            </form>
            <p className="text-center text-gray-500 text-xs">
              &copy;2021 Mental Health Status Analyzer
            </p>
          </div>
        </div>
      )}
    </>
  );
};

export default Login;
