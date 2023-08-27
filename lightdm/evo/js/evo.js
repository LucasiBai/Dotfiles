const powerOperations = {
	Shutdown: "󰤁",
	Restart: "",
	Hibernate: "󰙧",
	Suspend: "",
};

let timeWidgetMode = 1;
let currentUser;
let currentSession;

const LOG_IN_CLASS_STATE = "log-in"

function update_time() {
	$("dt").innerText =
		timeWidgetMode === 0
			? new Date().toLocaleDateString()
			: new Date().toLocaleTimeString();

  $("clock-time").innerText = getFormattedTime() 

  $("date-time").innerText = getFormattedDate()

}

this.addEventListener("load", () => {
	$("dt").addEventListener("click", () => {
		timeWidgetMode = timeWidgetMode === 0 ? 1 : 0;
		update_time();
	});
	document.querySelectorAll("[dropdown]").forEach((btn) => {
		const dropdown = btn.attributes.dropdown.value;
		btn.addEventListener("click", () => $(dropdown).classList.toggle("show"));
	});
	update_time();
	setInterval(() => update_time(), 1000);
	Object.entries(powerOperations)
		.filter(([o, _]) => lightdm[`can_${o.toLowerCase()}`])
		.forEach(([o, i]) =>
			$("powermenu").appendChild(
				make_menu_item(
					`<p class="icon" style="display: inline">${i}</p> ${o}`,
					() => lightdm[o.toLowerCase()](),
				),
			),
		);
	lightdm.users.forEach((usr) =>
		$("user-dropdown").appendChild(
			make_menu_item(
				`<img src="${usr.image}" class="sm-avatar"></img>${usr.display_name}`,
				() => set_user(usr),
			),
		),
	);
	lightdm.sessions.forEach((s) =>
		$("session-list").appendChild(make_menu_item(s.name, () => set_session(s))),
	);
	$("hostname").innerText = lightdm.hostname;
	set_user(lightdm.select_user || lightdm.users[0]);
  
  this.addEventListener("click",()=>{
    if(!$("login-box").className.includes(LOG_IN_CLASS_STATE)){
      showLogin()
    }
  })

  this.addEventListener("keydown",(event)=>{
    const {keyCode} = event

    const scapeKey = 27
    const showLoginKey = 13

    if(!$("login-box").className.includes(LOG_IN_CLASS_STATE) && keyCode === showLoginKey){
      showLogin()
    }
    if($("login-box").className.includes(LOG_IN_CLASS_STATE) && keyCode === scapeKey){
      hideLogin()
    }
  })
});


function make_menu_item(inner, click) {
	const d = document.createElement("div");
	d.addEventListener("click", click);
	d.innerHTML = inner;
	return d;
}

function toast(title, isErr) {
	const toast = document.createElement("div");
	if (isErr) toast.className = "err";
	toast.innerHTML = title;
	toast.addEventListener("click", () =>
		$("toast-container").removeChild(toast),
	);
	$("toast-container").appendChild(toast);
	setTimeout(() => {
		[1, 0.75, 0.5, 0.25].forEach((x) =>
			setTimeout(() => (toast.style.opacity = x), 25 / x),
		);
		setTimeout(() => {
			if ($("toast-container").contains(toast))
				$("toast-container").removeChild(toast);
		}, 125);
	}, 2000);
}

function authentication_complete() {
	$("login-btn").disabled = false;
	if (lightdm.is_authenticated) lightdm.start_session_sync(currentSession);
	else {
		if (lightdm._username) {
			lightdm.cancel_authentication();
		}
		if (currentUser) lightdm.start_authentication(currentUser.name);
		show_error("Wrong password!");
	}
}

function show_error(err) {
  const input  = $("password-box")
  input.className = "login-box--error"

  setTimeout(()=>{
    input.className =""
  },3000)
}

function show_prompt(text, type) {
	if (type === "password") {
		$("password-box").innerText = "";
		$("password-box").focus();
	} else toast(text, false);
}

function show_message(msg) {
	toast(msg, false);
}

function provide_secret() {
	password = $("password-box").value || null;
	if (password !== null) {
		$("login-btn").disabled = true;
		lightdm.respond(password);
	}
}

window.addEventListener("click", (e) => {
	if (!e.target.attributes.dropdown)
		Array.from(document.getElementsByClassName("drop-container"))
			.filter((drop) => drop.classList.contains("show"))
			.forEach((drop) => drop.classList.remove("show"));
});

function set_session(session) {
	currentSession = session;
	$("session").innerText = session.name;
}

function set_user(user) {
	currentUser = user;
	if (lightdm._username) {
		lightdm.cancel_authentication();
	}
	if (user) lightdm.start_authentication(user.name);
	set_session(
		currentUser.session
			? lightdm.sessions.find((s) => s.key === currentUser.session)
			: currentSession || lightdm.default_session,
	);
	$("avatar").src = user.image;
	$("name").textContent = user.display_name;
  $("password-box").focus();
}

function hideLogin(){
  $("login-box").className ="" 
  $("screen").className ="" 
  $("clock-box").className=""

  $("password-box").value = ""
}

function showLogin(){
  $("login-box").className = LOG_IN_CLASS_STATE
  $("screen").className = LOG_IN_CLASS_STATE
  $("clock-box").className = LOG_IN_CLASS_STATE

  $("password-box").value = ""
  $("password-box").focus()
}

function getFormattedTime() {
  const date = new Date();
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const amPm = hours >= 12 ? "PM" : "AM";
  
  hours = hours % 12 || 12;
  
  minutes = minutes < 10 ? "0" + minutes : minutes;
  
  const formattedTime = `${hours}:${minutes} ${amPm}`;
  
  return formattedTime;
}

function getFormattedDate() {
  const date = new Date();

  const options = { weekday: 'long', month: 'long', day: 'numeric' };
  const formattedDate = date.toLocaleDateString('en-US', options);

  return formattedDate;
}

function $(id) {
	return document.getElementById(id);
}
