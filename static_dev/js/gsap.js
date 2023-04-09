gsap.registerPlugin(ScrollTrigger);

// initialize the animation
const tl = gsap.timeline();
// set initial opacity to 0
gsap.set(".heading", {opacity: 0});
// add the animations
tl.to(".heading", {
    opacity: 1,
    duration: 3,
    ease: "power3.out"
})
tl.to(".heading", {
    scale: 1,
    duration: 3,
    ease: "elastic.out(3, 0.3)",
    delay: -1.5
});
    
// set initial opacity to 0
gsap.set(".card", {opacity: 0});

// animate opacity to 1 when card is in view
ScrollTrigger.batch(".card", {
    onEnter: (batch) => gsap.to(batch, {opacity: 1, stagger: 0.2, duration: 0.5}),
    start: "top 80%",
    end: "+=200",
    once: true,
    reversed:true,
});

// set initial scale to 0
gsap.set(".first-div", {scale: 0});

// animate to final scale when card is in view
ScrollTrigger.batch(".first-div", {
    onEnter: (batch) => gsap.to(batch, {scale: 1, stagger: 0.2, duration: 0.5}),
    start: "top 80%",
    end: "+=200",
    once: true
});

// set initial opacity to 0
gsap.set(".funct", {opacity: 0});

// animate opacity to 1 when funct is in view
ScrollTrigger.batch(".funct", {
    onEnter: (batch) => gsap.to(batch, {opacity: 1, stagger: 0.2, duration: 0.5}),
    start: "top 80%",
    end: "+=200",
    once: true,
    reversed:true,
});

//Accordion items
const accordionItems = document.querySelectorAll(".accordion-item");

accordionItems.forEach((item) => {
  const header = item.querySelector(".accordion-header");
  const content = item.querySelector(".accordion-body");

  // initialize the animation
  const acc = gsap.timeline({
    paused: true,
    defaults: { duration: 0.5, ease: "power3.out" }
  });

  // add the animation
  acc.to(content, { height: "auto" })
    .fromTo(content, { opacity: 0 }, { opacity: 1 });

  // add click event listener to header
  header.addEventListener("click", () => {
    if (item.classList.contains("active")) {
      item.classList.remove("active");
      acc.reverse();
    } else {
      item.classList.add("active");
      acc.play();
    }
  });
});

//button Register
const myLink = document.querySelector(".my-link");

myLink.addEventListener("mouseenter", () => {
  gsap.to(myLink, {
    duration: 0.3,
    backgroundColor: "#23BAC4",
    color: "#fff",
    borderColor: "#fff"
  });
});

myLink.addEventListener("mouseleave", () => {
  gsap.to(myLink, {
    duration: 0.3,
    backgroundColor: "#fff",
    color: "#109DFA",
    borderColor: "#00CCFF"
  });
});

//button RLogin
const myLogIn = document.querySelector(".my-login");

myLogIn.addEventListener("mouseenter", () => {
  gsap.to(myLogIn, {
    duration: 0.3,
    backgroundColor: "#B8B8B8",
    color: "#fff",
    borderColor: "#fff"
  });
});

myLogIn.addEventListener("mouseleave", () => {
  gsap.to(myLogIn, {
    duration: 0.3,
    backgroundColor: "#fff",
    color: "#B2B3B5",
    borderColor: "#808080"
  });
});

//Index Image
const myImage = document.querySelector(".my-image");

gsap.to(myImage, {
  duration: 2,
  scale: 1.2,
  //rotation: 360,
  borderRadius: "50%",
  boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.4)",
  onComplete: () => {
    gsap.to(myImage, {
      duration: 2,
      scale: 1,
      rotation: 0,
      borderRadius: "5px",
      boxShadow: "0px 0px 5px rgba(0, 0, 0, 0.2)"
    });
  }
});

// set initial opacity to 0
gsap.set(".index-div", {opacity: 0});

// animate opacity to 1 when card is in view
ScrollTrigger.batch(".index-div", {
  onEnter: (batch) => gsap.to(batch, {opacity: 1, stagger: 0.2, duration: 0.5}),
  start: "top 80%",
  end: "+=200",
  once: true
});