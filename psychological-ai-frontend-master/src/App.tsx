import "./App.css";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Redirect,
} from "react-router-dom";

// Components
import Home from "./Components/Home";
import Login from "./Components/Auth/Login";
import History from "./Components/History";
import { isAuthorized } from "./Components/Auth/AuthService";
import Register from "./Components/Auth/Register";
import Twitter from "./Components/Twitter";

function App() {
  return (
    <>
      <Router>
        <Switch>
          <Route
            exact
            path={"/"}
            render={() => {
              return isAuthorized() ? <Home /> : <Redirect to={"/login"} />;
            }}
          />
          <Route exact path={"/login"} component={Login} />
          <Route exact path={"/register"} component={Register} />
          <Route exact path={"/history"} component={History} />
          <Route exact path={"/twitter"} component={Twitter} />
        </Switch>
      </Router>
    </>
  );
}

export default App;
