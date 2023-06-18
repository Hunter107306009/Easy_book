import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import main from "./main";
import login from "./login";
import signup from "./signup";
import checkout from "./checkout";
import book_page from "./book_page";
import blacklist from "./blacklist";
import book_manage from "./book_manage";
import personal_page from "./personal_page";
import cus_modify from "./cus_modify";
import res_modify from "./res_modify";
import res_reRegister from "./res_reRegister";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={login} />
        <Route exact path="/main" component={main} />
        <Route exact path="/signup" component={signup} />
        <Route exact path="/checkout" component={checkout} />
        <Route exact path="/blacklist" component={blacklist} />
        <Route exact path="/book_page" component={book_page} />
        <Route exact path="/book_manage" component={book_manage} />
        <Route exact path="/personal_page" component={personal_page} />
        <Route exact path="/cus_modify" component={cus_modify} />
        <Route exact path="/res_modify" component={res_modify} />
        <Route exact path="/res_reRegister" component={res_reRegister} />
      </Switch>
    </Router>
  );
}

export default App;
