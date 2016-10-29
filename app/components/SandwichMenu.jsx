var Radium = require('radium');
var {Link, IndexLink} = require('react-router');
var RadiumLink = Radium(Link);
var React = require('react');
var Menu = require('react-burger-menu').slide;

// var RadiumLink = Radium(Link);

// @Radium
var SandwichMenu = React.createClass({
  // showSettings: function(e) {
  //   e.preventDefault();
  // },


  render: function () {
      return (
          <Menu width={ 200 }>

            {/* <a id="home" className="menu-item" href="/history">History</a>
            <a onClick={ this.showSettings } className="menu-item--small" href="">Settings</a> */}
            <RadiumLink className="menu-item" to="/history">History</RadiumLink>
        </Menu>

      );
  }
});


module.exports = SandwichMenu;