var React = require('react');
var ReactDOM = require('react-dom');
var {Router, Route, IndexRoute, hashHistory} = require('react-router');
var Feedback = require('Feedback');
var Home = require('Home');
var History = require('History');
var Login = require('Login');
var ShoppingCart = require('ShoppingCart');

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={Home}>
      <Route path="/feedback" component={Feedback}/>
      <Route path="/history" component={History}/>
      <Route path="/shoppingcart" component={ShoppingCart}/>
      <Route path="/login" component={Login}/>
    </Route>
  </Router>,
  document.getElementById('app')
);