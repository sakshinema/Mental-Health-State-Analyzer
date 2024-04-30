import { ILogin } from "../Common/Interfaces";
import axios from "axios";
import { baseUrl } from "../Common/Constants";

export const LoginHandler = (loginData: ILogin) => {
  return axios.post(baseUrl + "api/token/", loginData).then((res) => {
    if (res.data.access) {
      localStorage.setItem("auth", JSON.stringify(res.data));
    }
    return res.data;
  });
};

export const RegisterHandler = (registerData: ILogin) => {
  return axios.post(baseUrl + "register/", registerData).then((res) => {
    if (res.data.access) {
      localStorage.setItem("auth", JSON.stringify(res.data));
    }
    return res.data;
  });
};

export const LogoutHandler = () => {
  localStorage.removeItem("auth");
};

export const GetAuth = () => {
  return localStorage.getItem("auth");
};

export const isAuthorized = () => {
  const tokens = JSON.parse(localStorage.getItem("auth") as string);
  // We can even call to server to check whether the tokens present in the localStorage are valid
  if (tokens && tokens.access) return true;
  return false;
};
