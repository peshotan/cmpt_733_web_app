let express         = require("express"),
    app             = express(),
    bodyParser      = require("body-parser"),
    flash           = require("connect-flash"),
    PORT            = process.env.PORT || 3004,
    expressSanitizer = require("express-sanitizer");


app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(expressSanitizer());



//=========HomePage========
app.get("/",(req,res)=>{
    res.render("homepage");
});


//=========DashBoard============
app.get("/dashboards/1", (req,res) => {
    res.render("dashboards/dashboard1")
});

app.get("/dashboards/2", (req,res) => {
    res.render("dashboards/dashboard2")
});

app.get("/dashboards/3", (req,res) => {
    res.render("dashboards/dashboard3")
});

app.get("/dashboards/4", (req,res) => {
    res.render("dashboards/dashboard4")
});



//=================

app.listen(PORT, process.env.IP, function(){
   console.log(`The Team 404 Server has started! on ${PORT}`);
});