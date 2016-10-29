module.exports = {
  entry: './app/app.jsx',
  output: {
    path: __dirname,
    filename: './static/bundle.js'
  },
  resolve: {
    root: __dirname,
    alias: {
      Feedback: 'app/components/Feedback.jsx',
      Home: 'app/components/Home.jsx',
      History: 'app/components/History.jsx',
      Login: 'app/components/Login.jsx',
      LoginForm: 'app/components/LoginForm.jsx',
      Nav: 'app/components/Nav.jsx',
      SandwichMenu: 'app/components/SandwichMenu.jsx',
      SandwichMenuStyle: 'app/styles/SandwichMenu.css',
      ShoppingCart: 'app/components/ShoppingCart.jsx',
      WebStyle: 'app/styles/style.css',

    },
    extensions: ['', '.js', '.jsx', '.css'],
    path: __dirname + '/static',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        loader: 'babel-loader',
        query: {
          presets: ['react', 'es2015', 'stage-0']
        },
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
      },

    ]
  }

};