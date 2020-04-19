let express         = require("express"),
    app             = express(),
    bodyParser      = require("body-parser"),
    flash           = require("connect-flash"),
    PORT            = process.env.PORT || 3004,
    expressSanitizer= require("express-sanitizer");
    axios           = require("axios");
    path            = require('path');
    cookieParser    = require('cookie-parser');
    logger          = require('morgan');
    spawn           = require("child_process").spawn;
    createError     = require('http-errors');


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(expressSanitizer());



//getting weather data
let getWeatherData = async (req, res) => {
    const API_KEY_WEATHER = "please add your API Key here";
    try{
        const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=${API_KEY_WEATHER}`);
        // console.log(response);
        console.log("SUCESSS******************");
        let data = response.data;
        console.log(data);
        let url_prediction = `/model/pred?long=${data.long}&lat=${data.lat}&temp=${data.temperature}&prep=${data.precipitation}`
        res.render('dashboards/dashboard5',  {weatherData : data});
    } catch (err) {
        console.log(err)
    }
};

// predictions
app.get('/model/pred', (req, res) => {
    let n = req.query.long;
    let m = req.query.lat;
    let o = req.query.temp;
    let q = req.query.prep;

    //name of the model
    let name_of_mode = "file_name_containing the model";

    //path to model
    url_model = `./pythonModels/${name_of_model}`;

    //pass the parameters to
    var process = spawn('python',[`./python/${name_of_model}`, n, m, o, q] );

    process.stdout.on('data', data=> {
        let d = data.toString();
        let c = JSON.parse(d);
        res.json({"your answer is" : c})
    });
});
//=========HomePage========

// app.get("/api/pred", (req, res) => {
//     getWeatherData(req, res);
// });
//

// routes for new dashboard

app.get("/", (req,res) => {
    res.render("links/blankNew")
});

app.get("/generaltrends", (req,res) => {
    res.render("links/rose")
});

app.get("/provincial", (req,res) => {
    res.render("links/provincial")
});

app.get("/tables", (req,res) => {
    res.render("links/tables")
});

app.get("/averagedemand", (req,res) => {
    res.render("links/averagedemand")
});

app.get("/cityselection", (req,res) => {
    res.render("links/cityselection")
});

app.get("/contactus", (req,res) => {
    res.render("links/contactus")
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    next(createError(404));
});


// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.send("ERROR! please use the standard url - Team 3 eyed Raven");
});




//=================

app.listen(PORT, process.env.IP, function(){
   console.log(`The Team 404 Server has started! on ${PORT}`);
});