const AuthHeader = () => {
  const authTokens = JSON.parse(localStorage.getItem("auth") as string);

  if (authTokens && authTokens.access) {
    return { Authorization: "Bearer" + authTokens.access };
  }
  return {};
};

export default AuthHeader;
