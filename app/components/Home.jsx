var React = require('react');
var Nav = require('Nav');

var Home = React.createClass({
  render: function () {
      return (
        <div>
          <h2>
            Loaded from Home
          </h2>
            <Nav/>
            {this.props.children}
        </div>

      );
  }
});

module.exports = Home;