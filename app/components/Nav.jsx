var React = require('react');
var {Link, IndexLink} = require('react-router');
var Radium = require('radium');

var RadiumLink = Radium(Link);

var Nav = React.createClass({
  render: function () {
      return (
        <div>
          <h2>Nav Component</h2>
            <IndexLink to="/" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Home</IndexLink>
            <Link to ="/feedback" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Feedback</Link>
            <Link to ="/history" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>History</Link>
            <Link to ="/shoppingcart" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Shopping Cart</Link>
            <Link to ="/login" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Login</Link>
            {/* <a href="#/about">Go To About</a> */}
        </div>
      )
  }
});

module.exports = Nav;