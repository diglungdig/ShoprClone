var React = require('react');
// var bcrypt = require('bcryptjs');
var sha512 = require('js-sha512');

var LoginForm = React.createClass({
  onFormSubmit: function (e) {
    e.preventDefault();

    var updates = {};
    var UserName = this.refs.UserName.value;
    var Password = this.refs.Password.value;



    if (UserName.length < 8 || Password.length < 8) {
      console.log('Login error');
    }

    if (UserName.length > 0) {
      this.refs.UserName.value = '';
      updates.UserName = UserName;
      console.log('Login works');
    }

    if (Password.length > 0) {
      this.refs.Password.value = '';
      updates.Password = Password;
      // var salt = bcrypt.genSaltSync(10);
      // var hash = bcrypt.hashSync("B4c0/\/", salt);
      console.log('Password works');
      // console.log(hash);

      console.log(sha512(Password));
    }


    this.props.onNewData(updates);
  },
  render: function () {
    return (
      <form onSubmit={this.onFormSubmit}>
        <div>
          <input type="text" ref="UserName" placeholder="Enter UserName"/>
        </div>
        <div>
          <input type="password" ref="password" placeholder="Enter Password"></input>
        </div>
        <div>
          <button>Submit</button>
        </div>
      </form>
    );
  }
});

module.exports = LoginForm;