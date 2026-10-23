// Portfolio interactions: loader, starfield, cursor, typing roles, scroll-lit statement,
// counters, poster lightbox, journey tabs, copy email and the contact form.
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var data = {};
  try {
    data = JSON.parse(document.getElementById("site-data").textContent);
  } catch (e) {
    /* Keep defaults. */
  }

  // Loader: counts to 100, then slides away. Shown once per visit.
  var loader = document.getElementById("loader");
  var count = document.getElementById("loaderCount");
  var seen = false;
  try {
    seen = sessionStorage.getItem("loaderSeen") === "1";
    sessionStorage.setItem("loaderSeen", "1");
  } catch (e) {
    /* Storage can be blocked; show the loader. */
  }
  if (loader) {
    if (reduce || seen) {
      loader.remove();
    } else {
      var n = 0;
      var t = setInterval(function () {
        n = Math.min(100, n + Math.ceil(Math.random() * 12));
        count.textContent = n;
        if (n >= 100) {
          clearInterval(t);
          setTimeout(function () {
            loader.classList.add("is-done");
            setTimeout(function () { loader.remove(); }, 900);
          }, 150);
        }
      }, 55);
    }
  }

  // Starfield with gentle mouse parallax.
  var canvas = document.getElementById("stars");
  if (canvas) {
    var ctx = canvas.getContext("2d");
    var stars = [], w = 0, h = 0, mx = 0, my = 0;
    var size = function () {
      var r = canvas.getBoundingClientRect();
      var d = window.devicePixelRatio || 1;
      w = r.width; h = r.height;
      canvas.width = w * d; canvas.height = h * d;
      ctx.setTransform(d, 0, 0, d, 0, 0);
      stars = Array.from({ length: Math.round((w * h) / 5000) }, function () {
        return { x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.3 + 0.2, z: Math.random() * 0.8 + 0.2, tw: Math.random() * Math.PI * 2 };
      });
    };
    var draw = function (time) {
      ctx.clearRect(0, 0, w, h);
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i];
        if (!reduce) { s.y -= 0.06 * s.z; if (s.y < 0) s.y = h; }
        var a = 0.35 + 0.45 * Math.abs(Math.sin(s.tw + time / 1400));
        ctx.fillStyle = "rgba(214, 205, 255," + a + ")";
        ctx.beginPath();
        ctx.arc(s.x + mx * s.z * 18, s.y + my * s.z * 18, s.r, 0, Math.PI * 2);
        ctx.fill();
      }
      if (!reduce) requestAnimationFrame(draw);
    };
    size();
    requestAnimationFrame(draw);
    window.addEventListener("resize", size);
    window.addEventListener("mousemove", function (e) {
      mx = e.clientX / window.innerWidth - 0.5;
      my = e.clientY / window.innerHeight - 0.5;
    });
  }

  // Custom cursor, only once a mouse moves.
  var dot = document.getElementById("cursor");
  var ring = document.getElementById("cursorRing");
  if (dot && ring) {
    var rx = 0, ry = 0, tx = 0, ty = 0;
    window.addEventListener("mousemove", function (e) {
      document.body.classList.add("has-pointer");
      tx = e.clientX; ty = e.clientY;
      dot.style.transform = "translate(" + tx + "px," + ty + "px)";
    });
    (function follow() {
      rx += (tx - rx) * 0.18; ry += (ty - ry) * 0.18;
      ring.style.transform = "translate(" + rx + "px," + ry + "px)";
      requestAnimationFrame(follow);
    })();
    document.querySelectorAll("a, button, .card, .tech").forEach(function (el) {
      el.addEventListener("mouseenter", function () { ring.classList.add("is-hover"); });
      el.addEventListener("mouseleave", function () { ring.classList.remove("is-hover"); });
    });
  }

  // Phone menu.
  var menuBtn = document.getElementById("menuBtn");
  var menu = document.getElementById("mobileMenu");
  if (menuBtn && menu) {
    var setMenu = function (open) {
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      menuBtn.setAttribute("aria-label", open ? menuBtn.dataset.closeLabel : menuBtn.dataset.openLabel);
      document.body.classList.toggle("menu-open", open);
      if (open) {
        menu.hidden = false;
        requestAnimationFrame(function () { menu.classList.add("is-open"); });
      } else {
        menu.classList.remove("is-open");
        setTimeout(function () { if (!menu.classList.contains("is-open")) menu.hidden = true; }, 300);
      }
    };
    menuBtn.addEventListener("click", function () {
      setMenu(menuBtn.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menuBtn.getAttribute("aria-expanded") === "true") {
        setMenu(false);
        menuBtn.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 860 && menuBtn.getAttribute("aria-expanded") === "true") setMenu(false);
    });
  }

  // Stacked project cards: a card taller than the screen sticks once its bottom is visible,
  // so the whole card can be read before the next one slides over it.
  var cards = Array.prototype.slice.call(document.querySelectorAll(".card"));
  var nav = document.querySelector(".nav");
  var setStick = function () {
    var navH = nav ? nav.getBoundingClientRect().height : 64;
    cards.forEach(function (card, i) {
      var base = navH + 20 + i * (window.innerWidth > 860 ? 22 : 14);
      var fit = window.innerHeight - card.offsetHeight - 12;
      card.style.top = Math.min(base, fit) + "px";
    });
  };
  if (cards.length) {
    setStick();
    window.addEventListener("resize", setStick);
    window.addEventListener("load", setStick);
    document.querySelectorAll(".card img").forEach(function (img) { img.addEventListener("load", setStick); });
  }

  // Typing roles.
  var roles = data.roles || [];
  var typed = document.getElementById("typed");
  if (typed && roles.length > 1 && !reduce) {
    var ri = 0, ci = roles[0].length, del = true;
    setInterval(function () {
      if (del) {
        ci--;
        if (ci <= 0) { del = false; ri = (ri + 1) % roles.length; }
      } else {
        ci++;
        if (ci >= roles[ri].length + 14) del = true;
      }
      typed.textContent = roles[ri].slice(0, Math.max(0, Math.min(ci, roles[ri].length)));
    }, 70);
  }

  // Statement: words light up as the reader scrolls.
  var st = document.getElementById("statement");
  if (st && !reduce) {
    var walker = document.createTreeWalker(st, NodeFilter.SHOW_TEXT), nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var frag = document.createDocumentFragment();
      node.textContent.split(/(\s+)/).forEach(function (part) {
        if (/\S/.test(part)) {
          var s = document.createElement("span");
          s.className = "w";
          s.textContent = part;
          frag.appendChild(s);
        } else {
          frag.appendChild(document.createTextNode(part));
        }
      });
      node.parentNode.replaceChild(frag, node);
    });
    var words = st.querySelectorAll(".w");
    var lightWords = function () {
      var r = st.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = Math.min(1, Math.max(0, (vh * 0.85 - r.top) / (r.height + vh * 0.35)));
      var on = Math.round(p * words.length);
      words.forEach(function (w, i) { w.classList.toggle("on", i < on); });
    };
    window.addEventListener("scroll", lightWords, { passive: true });
    lightWords();
  }

  // Counters.
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        io.unobserve(en.target);
        var el = en.target, end = parseFloat(el.dataset.count), pre = el.dataset.prefix || "", s = null;
        (function step(ts) {
          if (!s) s = ts;
          var k = Math.min(1, (ts - s) / 1300);
          el.textContent = pre + Math.round(end * (1 - Math.pow(1 - k, 3)));
          if (k < 1) requestAnimationFrame(step);
        })(performance.now());
      });
    }, { threshold: 0.6 });
    document.querySelectorAll("[data-count]").forEach(function (c) { io.observe(c); });
  }

  // Poster lightbox.
  var lb = document.getElementById("lightbox");
  var lbImg = document.getElementById("lightboxImg");
  var lbClose = document.getElementById("lightboxClose");
  var lastBtn = null;
  if (lb && lbImg && lbClose) {
    var closeLb = function () {
      lb.hidden = true;
      document.body.style.overflow = "";
      if (lastBtn) lastBtn.focus();
    };
    document.querySelectorAll(".poster-btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        lastBtn = btn;
        lbImg.src = btn.dataset.full;
        lbImg.alt = btn.querySelector("img").alt;
        lb.hidden = false;
        document.body.style.overflow = "hidden";
        lbClose.focus();
      });
    });
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
    lbClose.addEventListener("click", closeLb);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !lb.hidden) closeLb();
    });
  }

  // Journey tabs, with arrow-key support.
  var tabs = Array.prototype.slice.call(document.querySelectorAll(".tab"));
  var selectTab = function (tab) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute("aria-selected", on ? "true" : "false");
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
  };
  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () { selectTab(tab); });
    tab.addEventListener("keydown", function (e) {
      var next = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (!next) return;
      e.preventDefault();
      var target = tabs[(i + next + tabs.length) % tabs.length];
      selectTab(target);
      target.focus();
    });
  });

  // Copy email.
  var copyBtn = document.getElementById("copyEmail");
  var emailText = document.getElementById("emailText");
  if (copyBtn && emailText) {
    copyBtn.addEventListener("click", function () {
      var done = function (label) {
        copyBtn.textContent = label;
        setTimeout(function () { copyBtn.textContent = data.copy || "Copy"; }, 2000);
      };
      var select = function () {
        var r = document.createRange();
        r.selectNodeContents(emailText);
        var s = window.getSelection();
        s.removeAllRanges();
        s.addRange(r);
        done(data.selected || "Selected");
      };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(emailText.textContent.trim()).then(function () { done(data.copied || "Copied"); }, select);
      } else {
        select();
      }
    });
  }

  // Contact form: opens the visitor's email app with the message filled in.
  var form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var name = form.elements.name.value.trim();
      var from = form.elements.email.value.trim();
      var msg = form.elements.message.value.trim();
      var body = msg + "\n\n" + name + "\n" + from;
      window.location.href = "mailto:" + data.email +
        "?subject=" + encodeURIComponent(data.subject + ": " + name) +
        "&body=" + encodeURIComponent(body);
      document.getElementById("formNote").hidden = false;
    });
  }
})();
