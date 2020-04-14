let express         = require("express"),
    app             = express(),
    bodyParser      = require("body-parser"),
    flash           = require("connect-flash"),
    PORT            = process.env.PORT || 3004,
    expressSanitizer = require("express-sanitizer");
    axios             = require("axios");


let getWeatherData = async (req, res) => {
    try{
        const response = await axios.get("http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=8456705436bca69bf9423d0bc84b778e");
        // console.log(response);
        console.log("SUCESSS******************");
        let data = response.data;
        console.log(data);
        res.render('dashboards/dashboard5',  {weatherData : data});
    } catch (err) {
        console.log(err)
    }
};




app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(expressSanitizer());



//=========HomePage========
// app.get("/",(req,res)=>{
//     res.render("homepage");
// });
//
//
// app.get("/api/pred", (req, res) => {
//     getWeatherData(req, res);
// });



//=========DashBoard============
// app.get("/dashboards/1", (req,res) => {
//     res.render("dashboards/dashboard1")
// });
//
// app.get("/dashboards/2", (req,res) => {
//     res.render("dashboards/dashboard2")
// });
//
// app.get("/dashboards/3", (req,res) => {
//     res.render("dashboards/dashboard3")
// });
//
// app.get("/dashboards/4", (req,res) => {
//     res.render("dashboards/dashboard4")
// });
//
// app.get("/dashboards/5", (req,res) => {
//     res.render("dashboards/dashboard5", {weatherData : "1"})
// });

// routes for new dashboard

app.get("/", (req,res) => {
    res.render("links/blankNew")
});

app.get("./generaltrends", (req,res) => {
    res.render("links/rose")
});

app.get("./provincial", (req,res) => {
    res.render("links/provincial")
});

app.get("./tables", (req,res) => {
    res.render("links/tables")
});

app.get("./averagedemand", (req,res) => {
    res.render("links/averagedemand")
});



//=================

app.listen(PORT, process.env.IP, function(){
   console.log(`The Team 404 Server has started! on ${PORT}`);
});