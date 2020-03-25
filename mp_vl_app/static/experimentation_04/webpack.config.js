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
                use: ['babel-loader']
            }
        ]
    },
    resolve: {
        extensions: [ '.js' ]
    }

}
