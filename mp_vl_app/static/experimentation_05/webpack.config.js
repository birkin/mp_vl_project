const path = require( 'path');

module.exports = {
    entry: {
        app: './src/index.js'
    },
    watch: true,
    devtool: 'source-map',
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist')
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_module/,
                // use: ['babel-loader'],
                // below is a change from the video, to get the react compilation to work
                use: [
                    {
                      loader: 'babel-loader',
                      options: {
                        presets: ['@babel/react']
                      }
                    }
                ]
            },
            {
              test: /\.css$/i,
              use: ['style-loader', 'css-loader'],
            }
        ]
    },
    resolve: {
        extensions: [ '.js' ]
    }

}
