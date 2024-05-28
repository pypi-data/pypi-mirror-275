const {
  SvelteComponent: Sl,
  append: Ze,
  attr: A,
  detach: zl,
  init: Fl,
  insert: Ll,
  noop: Ge,
  safe_not_equal: Ml,
  set_style: R,
  svg_element: qe
} = window.__gradio__svelte__internal;
function Vl(l) {
  let e, t, n, i;
  return {
    c() {
      e = qe("svg"), t = qe("g"), n = qe("path"), i = qe("path"), A(n, "d", "M18,6L6.087,17.913"), R(n, "fill", "none"), R(n, "fill-rule", "nonzero"), R(n, "stroke-width", "2px"), A(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), A(i, "d", "M4.364,4.364L19.636,19.636"), R(i, "fill", "none"), R(i, "fill-rule", "nonzero"), R(i, "stroke-width", "2px"), A(e, "width", "100%"), A(e, "height", "100%"), A(e, "viewBox", "0 0 24 24"), A(e, "version", "1.1"), A(e, "xmlns", "http://www.w3.org/2000/svg"), A(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), A(e, "xml:space", "preserve"), A(e, "stroke", "currentColor"), R(e, "fill-rule", "evenodd"), R(e, "clip-rule", "evenodd"), R(e, "stroke-linecap", "round"), R(e, "stroke-linejoin", "round");
    },
    m(f, s) {
      Ll(f, e, s), Ze(e, t), Ze(t, n), Ze(e, i);
    },
    p: Ge,
    i: Ge,
    o: Ge,
    d(f) {
      f && zl(e);
    }
  };
}
class jl extends Sl {
  constructor(e) {
    super(), Fl(this, e, null, Vl, Ml, {});
  }
}
const {
  SvelteComponent: Il,
  append: rt,
  attr: B,
  detach: Nl,
  init: El,
  insert: Dl,
  noop: Te,
  safe_not_equal: Bl,
  svg_element: Ue
} = window.__gradio__svelte__internal;
function Pl(l) {
  let e, t, n;
  return {
    c() {
      e = Ue("svg"), t = Ue("path"), n = Ue("polyline"), B(t, "d", "M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"), B(n, "points", "13 2 13 9 20 9"), B(e, "xmlns", "http://www.w3.org/2000/svg"), B(e, "width", "100%"), B(e, "height", "100%"), B(e, "viewBox", "0 0 24 24"), B(e, "fill", "none"), B(e, "stroke", "currentColor"), B(e, "stroke-width", "1.5"), B(e, "stroke-linecap", "round"), B(e, "stroke-linejoin", "round"), B(e, "class", "feather feather-file");
    },
    m(i, f) {
      Dl(i, e, f), rt(e, t), rt(e, n);
    },
    p: Te,
    i: Te,
    o: Te,
    d(i) {
      i && Nl(e);
    }
  };
}
class Zl extends Il {
  constructor(e) {
    super(), El(this, e, null, Pl, Bl, {});
  }
}
const {
  SvelteComponent: Gl,
  assign: Tl,
  create_slot: Ul,
  detach: Al,
  element: Ol,
  get_all_dirty_from_scope: Hl,
  get_slot_changes: Jl,
  get_spread_update: Wl,
  init: Xl,
  insert: Yl,
  safe_not_equal: Rl,
  set_dynamic_element_data: at,
  set_style: D,
  toggle_class: K,
  transition_in: el,
  transition_out: tl,
  update_slot_base: Kl
} = window.__gradio__svelte__internal;
function Ql(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), f = Ul(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let s = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-nl1om8"
    }
  ], r = {};
  for (let o = 0; o < s.length; o += 1)
    r = Tl(r, s[o]);
  return {
    c() {
      e = Ol(
        /*tag*/
        l[14]
      ), f && f.c(), at(
        /*tag*/
        l[14]
      )(e, r), K(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), K(
        e,
        "padded",
        /*padding*/
        l[6]
      ), K(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), K(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), K(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), D(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), D(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), D(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), D(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), D(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), D(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), D(e, "border-width", "var(--block-border-width)");
    },
    m(o, a) {
      Yl(o, e, a), f && f.m(e, null), n = !0;
    },
    p(o, a) {
      f && f.p && (!n || a & /*$$scope*/
      131072) && Kl(
        f,
        i,
        o,
        /*$$scope*/
        o[17],
        n ? Jl(
          i,
          /*$$scope*/
          o[17],
          a,
          null
        ) : Hl(
          /*$$scope*/
          o[17]
        ),
        null
      ), at(
        /*tag*/
        o[14]
      )(e, r = Wl(s, [
        (!n || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          o[7]
        ) },
        (!n || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          o[2]
        ) },
        (!n || a & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        o[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), K(
        e,
        "hidden",
        /*visible*/
        o[10] === !1
      ), K(
        e,
        "padded",
        /*padding*/
        o[6]
      ), K(
        e,
        "border_focus",
        /*border_mode*/
        o[5] === "focus"
      ), K(
        e,
        "border_contrast",
        /*border_mode*/
        o[5] === "contrast"
      ), K(e, "hide-container", !/*explicit_call*/
      o[8] && !/*container*/
      o[9]), a & /*height*/
      1 && D(
        e,
        "height",
        /*get_dimension*/
        o[15](
          /*height*/
          o[0]
        )
      ), a & /*width*/
      2 && D(e, "width", typeof /*width*/
      o[1] == "number" ? `calc(min(${/*width*/
      o[1]}px, 100%))` : (
        /*get_dimension*/
        o[15](
          /*width*/
          o[1]
        )
      )), a & /*variant*/
      16 && D(
        e,
        "border-style",
        /*variant*/
        o[4]
      ), a & /*allow_overflow*/
      2048 && D(
        e,
        "overflow",
        /*allow_overflow*/
        o[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && D(
        e,
        "flex-grow",
        /*scale*/
        o[12]
      ), a & /*min_width*/
      8192 && D(e, "min-width", `calc(min(${/*min_width*/
      o[13]}px, 100%))`);
    },
    i(o) {
      n || (el(f, o), n = !0);
    },
    o(o) {
      tl(f, o), n = !1;
    },
    d(o) {
      o && Al(e), f && f.d(o);
    }
  };
}
function xl(l) {
  let e, t = (
    /*tag*/
    l[14] && Ql(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (el(t, n), e = !0);
    },
    o(n) {
      tl(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function $l(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: f = void 0 } = e, { width: s = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: o = [] } = e, { variant: a = "solid" } = e, { border_mode: c = "base" } = e, { padding: _ = !0 } = e, { type: d = "normal" } = e, { test_id: h = void 0 } = e, { explicit_call: g = !1 } = e, { container: y = !0 } = e, { visible: C = !0 } = e, { allow_overflow: z = !0 } = e, { scale: m = null } = e, { min_width: u = 0 } = e, k = d === "fieldset" ? "fieldset" : "div";
  const b = (w) => {
    if (w !== void 0) {
      if (typeof w == "number")
        return w + "px";
      if (typeof w == "string")
        return w;
    }
  };
  return l.$$set = (w) => {
    "height" in w && t(0, f = w.height), "width" in w && t(1, s = w.width), "elem_id" in w && t(2, r = w.elem_id), "elem_classes" in w && t(3, o = w.elem_classes), "variant" in w && t(4, a = w.variant), "border_mode" in w && t(5, c = w.border_mode), "padding" in w && t(6, _ = w.padding), "type" in w && t(16, d = w.type), "test_id" in w && t(7, h = w.test_id), "explicit_call" in w && t(8, g = w.explicit_call), "container" in w && t(9, y = w.container), "visible" in w && t(10, C = w.visible), "allow_overflow" in w && t(11, z = w.allow_overflow), "scale" in w && t(12, m = w.scale), "min_width" in w && t(13, u = w.min_width), "$$scope" in w && t(17, i = w.$$scope);
  }, [
    f,
    s,
    r,
    o,
    a,
    c,
    _,
    h,
    g,
    y,
    C,
    z,
    m,
    u,
    k,
    b,
    d,
    i,
    n
  ];
}
class en extends Gl {
  constructor(e) {
    super(), Xl(this, e, $l, xl, Rl, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: tn,
  append: Ae,
  attr: Se,
  create_component: ln,
  destroy_component: nn,
  detach: sn,
  element: ct,
  init: on,
  insert: fn,
  mount_component: rn,
  safe_not_equal: an,
  set_data: cn,
  space: _n,
  text: un,
  toggle_class: ne,
  transition_in: dn,
  transition_out: mn
} = window.__gradio__svelte__internal;
function hn(l) {
  let e, t, n, i, f, s;
  return n = new /*Icon*/
  l[1]({}), {
    c() {
      e = ct("label"), t = ct("span"), ln(n.$$.fragment), i = _n(), f = un(
        /*label*/
        l[0]
      ), Se(t, "class", "svelte-9gxdi0"), Se(e, "for", ""), Se(e, "data-testid", "block-label"), Se(e, "class", "svelte-9gxdi0"), ne(e, "hide", !/*show_label*/
      l[2]), ne(e, "sr-only", !/*show_label*/
      l[2]), ne(
        e,
        "float",
        /*float*/
        l[4]
      ), ne(
        e,
        "hide-label",
        /*disable*/
        l[3]
      );
    },
    m(r, o) {
      fn(r, e, o), Ae(e, t), rn(n, t, null), Ae(e, i), Ae(e, f), s = !0;
    },
    p(r, [o]) {
      (!s || o & /*label*/
      1) && cn(
        f,
        /*label*/
        r[0]
      ), (!s || o & /*show_label*/
      4) && ne(e, "hide", !/*show_label*/
      r[2]), (!s || o & /*show_label*/
      4) && ne(e, "sr-only", !/*show_label*/
      r[2]), (!s || o & /*float*/
      16) && ne(
        e,
        "float",
        /*float*/
        r[4]
      ), (!s || o & /*disable*/
      8) && ne(
        e,
        "hide-label",
        /*disable*/
        r[3]
      );
    },
    i(r) {
      s || (dn(n.$$.fragment, r), s = !0);
    },
    o(r) {
      mn(n.$$.fragment, r), s = !1;
    },
    d(r) {
      r && sn(e), nn(n);
    }
  };
}
function gn(l, e, t) {
  let { label: n = null } = e, { Icon: i } = e, { show_label: f = !0 } = e, { disable: s = !1 } = e, { float: r = !0 } = e;
  return l.$$set = (o) => {
    "label" in o && t(0, n = o.label), "Icon" in o && t(1, i = o.Icon), "show_label" in o && t(2, f = o.show_label), "disable" in o && t(3, s = o.disable), "float" in o && t(4, r = o.float);
  }, [n, i, f, s, r];
}
class bn extends tn {
  constructor(e) {
    super(), on(this, e, gn, hn, an, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: pn,
  append: Ye,
  attr: ee,
  bubble: wn,
  create_component: kn,
  destroy_component: vn,
  detach: ll,
  element: Re,
  init: yn,
  insert: nl,
  listen: Cn,
  mount_component: qn,
  safe_not_equal: Sn,
  set_data: zn,
  set_style: ae,
  space: Fn,
  text: Ln,
  toggle_class: N,
  transition_in: Mn,
  transition_out: Vn
} = window.__gradio__svelte__internal;
function _t(l) {
  let e, t;
  return {
    c() {
      e = Re("span"), t = Ln(
        /*label*/
        l[1]
      ), ee(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      nl(n, e, i), Ye(e, t);
    },
    p(n, i) {
      i & /*label*/
      2 && zn(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && ll(e);
    }
  };
}
function jn(l) {
  let e, t, n, i, f, s, r, o = (
    /*show_label*/
    l[2] && _t(l)
  );
  return i = new /*Icon*/
  l[0]({}), {
    c() {
      e = Re("button"), o && o.c(), t = Fn(), n = Re("div"), kn(i.$$.fragment), ee(n, "class", "svelte-1lrphxw"), N(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), N(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), N(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], ee(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), ee(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), ee(
        e,
        "title",
        /*label*/
        l[1]
      ), ee(e, "class", "svelte-1lrphxw"), N(
        e,
        "pending",
        /*pending*/
        l[3]
      ), N(
        e,
        "padded",
        /*padded*/
        l[5]
      ), N(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), N(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), ae(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), ae(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), ae(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(a, c) {
      nl(a, e, c), o && o.m(e, null), Ye(e, t), Ye(e, n), qn(i, n, null), f = !0, s || (r = Cn(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), s = !0);
    },
    p(a, [c]) {
      /*show_label*/
      a[2] ? o ? o.p(a, c) : (o = _t(a), o.c(), o.m(e, t)) : o && (o.d(1), o = null), (!f || c & /*size*/
      16) && N(
        n,
        "small",
        /*size*/
        a[4] === "small"
      ), (!f || c & /*size*/
      16) && N(
        n,
        "large",
        /*size*/
        a[4] === "large"
      ), (!f || c & /*size*/
      16) && N(
        n,
        "medium",
        /*size*/
        a[4] === "medium"
      ), (!f || c & /*disabled*/
      128) && (e.disabled = /*disabled*/
      a[7]), (!f || c & /*label*/
      2) && ee(
        e,
        "aria-label",
        /*label*/
        a[1]
      ), (!f || c & /*hasPopup*/
      256) && ee(
        e,
        "aria-haspopup",
        /*hasPopup*/
        a[8]
      ), (!f || c & /*label*/
      2) && ee(
        e,
        "title",
        /*label*/
        a[1]
      ), (!f || c & /*pending*/
      8) && N(
        e,
        "pending",
        /*pending*/
        a[3]
      ), (!f || c & /*padded*/
      32) && N(
        e,
        "padded",
        /*padded*/
        a[5]
      ), (!f || c & /*highlight*/
      64) && N(
        e,
        "highlight",
        /*highlight*/
        a[6]
      ), (!f || c & /*transparent*/
      512) && N(
        e,
        "transparent",
        /*transparent*/
        a[9]
      ), c & /*disabled, _color*/
      4224 && ae(e, "color", !/*disabled*/
      a[7] && /*_color*/
      a[12] ? (
        /*_color*/
        a[12]
      ) : "var(--block-label-text-color)"), c & /*disabled, background*/
      1152 && ae(e, "--bg-color", /*disabled*/
      a[7] ? "auto" : (
        /*background*/
        a[10]
      )), c & /*offset*/
      2048 && ae(
        e,
        "margin-left",
        /*offset*/
        a[11] + "px"
      );
    },
    i(a) {
      f || (Mn(i.$$.fragment, a), f = !0);
    },
    o(a) {
      Vn(i.$$.fragment, a), f = !1;
    },
    d(a) {
      a && ll(e), o && o.d(), vn(i), s = !1, r();
    }
  };
}
function In(l, e, t) {
  let n, { Icon: i } = e, { label: f = "" } = e, { show_label: s = !1 } = e, { pending: r = !1 } = e, { size: o = "small" } = e, { padded: a = !0 } = e, { highlight: c = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: d = !1 } = e, { color: h = "var(--block-label-text-color)" } = e, { transparent: g = !1 } = e, { background: y = "var(--background-fill-primary)" } = e, { offset: C = 0 } = e;
  function z(m) {
    wn.call(this, l, m);
  }
  return l.$$set = (m) => {
    "Icon" in m && t(0, i = m.Icon), "label" in m && t(1, f = m.label), "show_label" in m && t(2, s = m.show_label), "pending" in m && t(3, r = m.pending), "size" in m && t(4, o = m.size), "padded" in m && t(5, a = m.padded), "highlight" in m && t(6, c = m.highlight), "disabled" in m && t(7, _ = m.disabled), "hasPopup" in m && t(8, d = m.hasPopup), "color" in m && t(13, h = m.color), "transparent" in m && t(9, g = m.transparent), "background" in m && t(10, y = m.background), "offset" in m && t(11, C = m.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = c ? "var(--color-accent)" : h);
  }, [
    i,
    f,
    s,
    r,
    o,
    a,
    c,
    _,
    d,
    g,
    y,
    C,
    n,
    h,
    z
  ];
}
class Nn extends pn {
  constructor(e) {
    super(), yn(this, e, In, jn, Sn, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5,
      highlight: 6,
      disabled: 7,
      hasPopup: 8,
      color: 13,
      transparent: 9,
      background: 10,
      offset: 11
    });
  }
}
const En = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], ut = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
En.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: ut[e][t],
      secondary: ut[e][n]
    }
  }),
  {}
);
const {
  SvelteComponent: Dn,
  append: dt,
  attr: ce,
  detach: Bn,
  init: Pn,
  insert: Zn,
  noop: Oe,
  safe_not_equal: Gn,
  set_style: _e,
  svg_element: He
} = window.__gradio__svelte__internal;
function Tn(l) {
  let e, t, n;
  return {
    c() {
      e = He("svg"), t = He("g"), n = He("path"), ce(n, "d", "M12.7,24.033C12.256,24.322 11.806,24.339 11.351,24.084C10.896,23.829 10.668,23.434 10.667,22.9L10.667,9.1C10.667,8.567 10.895,8.172 11.351,7.916C11.807,7.66 12.256,7.677 12.7,7.967L23.567,14.867C23.967,15.133 24.167,15.511 24.167,16C24.167,16.489 23.967,16.867 23.567,17.133L12.7,24.033Z"), _e(n, "fill", "currentColor"), _e(n, "fill-rule", "nonzero"), ce(t, "transform", "matrix(1,0,0,1,-10.6667,-7.73588)"), ce(e, "width", "100%"), ce(e, "height", "100%"), ce(e, "viewBox", "0 0 14 17"), ce(e, "version", "1.1"), _e(e, "fill-rule", "evenodd"), _e(e, "clip-rule", "evenodd"), _e(e, "stroke-linejoin", "round"), _e(e, "stroke-miterlimit", "2");
    },
    m(i, f) {
      Zn(i, e, f), dt(e, t), dt(t, n);
    },
    p: Oe,
    i: Oe,
    o: Oe,
    d(i) {
      i && Bn(e);
    }
  };
}
class Un extends Dn {
  constructor(e) {
    super(), Pn(this, e, null, Tn, Gn, {});
  }
}
const {
  SvelteComponent: An,
  attr: mt,
  detach: On,
  element: Hn,
  init: Jn,
  insert: Wn,
  listen: ht,
  noop: gt,
  run_all: Xn,
  safe_not_equal: Yn,
  toggle_class: bt
} = window.__gradio__svelte__internal, { createEventDispatcher: Rn } = window.__gradio__svelte__internal;
function Kn(l) {
  let e, t, n;
  return {
    c() {
      e = Hn("input"), mt(e, "type", "checkbox"), e.disabled = /*disabled*/
      l[1], mt(e, "class", "svelte-34z85b"), bt(
        e,
        "disabled",
        /*disabled*/
        l[1] && !/*value*/
        l[0]
      );
    },
    m(i, f) {
      Wn(i, e, f), e.checked = /*value*/
      l[0], t || (n = [
        ht(
          e,
          "change",
          /*input_change_handler*/
          l[3]
        ),
        ht(
          e,
          "input",
          /*input_handler*/
          l[4]
        )
      ], t = !0);
    },
    p(i, [f]) {
      f & /*disabled*/
      2 && (e.disabled = /*disabled*/
      i[1]), f & /*value*/
      1 && (e.checked = /*value*/
      i[0]), f & /*disabled, value*/
      3 && bt(
        e,
        "disabled",
        /*disabled*/
        i[1] && !/*value*/
        i[0]
      );
    },
    i: gt,
    o: gt,
    d(i) {
      i && On(e), t = !1, Xn(n);
    }
  };
}
function Qn(l, e, t) {
  let { value: n } = e, { disabled: i } = e;
  const f = Rn();
  function s() {
    n = this.checked, t(0, n);
  }
  const r = () => f("change", !n);
  return l.$$set = (o) => {
    "value" in o && t(0, n = o.value), "disabled" in o && t(1, i = o.disabled);
  }, [n, i, f, s, r];
}
class xn extends An {
  constructor(e) {
    super(), Jn(this, e, Qn, Kn, Yn, { value: 0, disabled: 1 });
  }
}
const pt = "data:image/svg+xml,%3csvg%20xmlns='http://www.w3.org/2000/svg'%20width='32'%20height='32'%20viewBox='0%200%2024%2024'%3e%3cpath%20fill='%23888888'%20d='M6%202c-1.1%200-1.99.9-1.99%202L4%2020c0%201.1.89%202%201.99%202H18c1.1%200%202-.9%202-2V8l-6-6H6zm7%207V3.5L18.5%209H13z'/%3e%3c/svg%3e", wt = "data:image/svg+xml,%3c?xml%20version='1.0'%20encoding='UTF-8'%20standalone='no'?%3e%3csvg%20viewBox='0%200%2032%2032'%20version='1.1'%20id='svg7'%20sodipodi:docname='light-folder-new.svg'%20inkscape:version='1.3.2%20(091e20e,%202023-11-25)'%20xmlns:inkscape='http://www.inkscape.org/namespaces/inkscape'%20xmlns:sodipodi='http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:svg='http://www.w3.org/2000/svg'%3e%3csodipodi:namedview%20id='namedview7'%20pagecolor='%23ffffff'%20bordercolor='%23000000'%20borderopacity='0.25'%20inkscape:showpageshadow='2'%20inkscape:pageopacity='0.0'%20inkscape:pagecheckerboard='0'%20inkscape:deskcolor='%23d1d1d1'%20inkscape:zoom='7.375'%20inkscape:cx='15.932203'%20inkscape:cy='16'%20inkscape:window-width='1312'%20inkscape:window-height='529'%20inkscape:window-x='0'%20inkscape:window-y='38'%20inkscape:window-maximized='0'%20inkscape:current-layer='svg7'%20/%3e%3cdefs%20id='defs6'%3e%3cclipPath%20id='clipPath1'%3e%3cpath%20d='m69.63%2012.145h-.052c-22.727-.292-46.47%204.077-46.709%204.122-2.424.451-4.946%202.974-5.397%205.397-.044.237-4.414%2023.983-4.122%2046.71-.292%2022.777%204.078%2046.523%204.122%2046.761.451%202.423%202.974%204.945%205.398%205.398.237.044%2023.982%204.413%2046.709%204.121%2022.779.292%2046.524-4.077%2046.761-4.121%202.423-.452%204.946-2.976%205.398-5.399.044-.236%204.413-23.981%204.121-46.709.292-22.777-4.077-46.523-4.121-46.761-.453-2.423-2.976-4.946-5.398-5.397-.238-.045-23.984-4.414-46.71-4.122'%20id='path1'%20/%3e%3c/clipPath%3e%3clinearGradient%20gradientUnits='userSpaceOnUse'%20y2='352.98'%20x2='-601.15'%20y1='663.95'%20x1='-591.02'%20id='2'%3e%3cstop%20stop-color='%23a0a0a0'%20id='stop1'%20/%3e%3cstop%20offset='1'%20stop-color='%23aaa'%20id='stop2'%20/%3e%3c/linearGradient%3e%3clinearGradient%20gradientUnits='userSpaceOnUse'%20y2='354.29'%20x2='-704.05'%20y1='647.77'%20x1='-701.19'%20id='1'%3e%3cstop%20stop-color='%23acabab'%20id='stop3'%20/%3e%3cstop%20offset='1'%20stop-color='%23d4d4d4'%20id='stop4'%20/%3e%3c/linearGradient%3e%3clinearGradient%20id='0'%20x1='59.12'%20y1='-19.888'%20x2='59.15'%20y2='-37.783'%20gradientUnits='userSpaceOnUse'%20gradientTransform='matrix(4.17478%200%200%204.16765-1069.7%20447.73)'%3e%3cstop%20stop-color='%23a0a0a0'%20id='stop5'%20/%3e%3cstop%20offset='1'%20stop-color='%23bdbdbd'%20id='stop6'%20/%3e%3c/linearGradient%3e%3c/defs%3e%3cg%20transform='matrix(.07089%200%200%20.07017%2023.295-40.67)'%20fill='%2360aae5'%20id='g7'%20style='fill:%23888888;fill-opacity:1'%3e%3cpath%20transform='matrix(.7872%200%200%20.79524%20415.34%20430.11)'%20d='m-884.1%20294.78c-4.626%200-8.349%203.718-8.349%208.335v161.41l468.19%201v-121.2c0-4.618-3.724-8.335-8.35-8.335h-272.65c-8.51.751-9.607-.377-13.812-5.981-5.964-7.968-14.969-21.443-20.84-29.21-4.712-6.805-5.477-6.02-13.292-6.02z'%20fill='url(%230)'%20color='%23000'%20id='path6'%20style='fill:%23888888;fill-opacity:1'%20/%3e%3crect%20transform='matrix(.7872%200%200%20.79524%20415.34%20430.11)'%20y='356.85'%20x='-890.28'%20height='295.13'%20width='463.85'%20fill='url(%231)'%20stroke='url(%231)'%20stroke-width='2.378'%20rx='9.63'%20id='rect6'%20style='fill:%23888888;fill-opacity:1'%20/%3e%3crect%20width='463.85'%20height='295.13'%20x='-890.28'%20y='356.85'%20transform='matrix(.7872%200%200%20.79524%20415.34%20430.11)'%20fill='none'%20stroke='url(%232)'%20stroke-linejoin='round'%20stroke-linecap='round'%20stroke-width='5.376'%20rx='9.63'%20id='rect7'%20style='fill:%23888888;fill-opacity:1'%20/%3e%3c/g%3e%3c/svg%3e", {
  SvelteComponent: $n,
  append: oe,
  attr: Z,
  bubble: ei,
  check_outros: Ke,
  create_component: lt,
  destroy_component: nt,
  destroy_each: ti,
  detach: Ee,
  element: be,
  ensure_array_like: kt,
  group_outros: Qe,
  init: li,
  insert: De,
  listen: vt,
  mount_component: it,
  noop: yt,
  run_all: ni,
  safe_not_equal: ii,
  set_data: si,
  space: ze,
  src_url_equal: Ct,
  stop_propagation: oi,
  text: fi,
  toggle_class: qt,
  transition_in: J,
  transition_out: te
} = window.__gradio__svelte__internal, { createEventDispatcher: ri } = window.__gradio__svelte__internal;
function St(l, e, t) {
  const n = l.slice();
  return n[24] = e[t].type, n[25] = e[t].name, n[26] = e[t].valid, n[28] = t, n;
}
function ai(l) {
  let e, t, n;
  return {
    c() {
      e = be("span"), t = be("img"), Ct(t.src, n = /*name*/
      l[25] === "." ? wt : pt) || Z(t, "src", n), Z(t, "alt", "file icon"), Z(t, "class", "svelte-zlvxd5"), Z(e, "class", "file-icon svelte-zlvxd5");
    },
    m(i, f) {
      De(i, e, f), oe(e, t);
    },
    p(i, f) {
      f & /*content*/
      64 && !Ct(t.src, n = /*name*/
      i[25] === "." ? wt : pt) && Z(t, "src", n);
    },
    i: yt,
    o: yt,
    d(i) {
      i && Ee(e);
    }
  };
}
function ci(l) {
  let e, t, n, i, f;
  t = new Un({});
  function s() {
    return (
      /*click_handler*/
      l[15](
        /*i*/
        l[28]
      )
    );
  }
  function r(...o) {
    return (
      /*keydown_handler*/
      l[16](
        /*i*/
        l[28],
        ...o
      )
    );
  }
  return {
    c() {
      e = be("span"), lt(t.$$.fragment), Z(e, "class", "icon svelte-zlvxd5"), Z(e, "role", "button"), Z(e, "aria-label", "expand directory"), Z(e, "tabindex", "0"), qt(e, "hidden", !/*opened_folders*/
      l[7].includes(
        /*i*/
        l[28]
      ));
    },
    m(o, a) {
      De(o, e, a), it(t, e, null), n = !0, i || (f = [
        vt(e, "click", oi(s)),
        vt(e, "keydown", r)
      ], i = !0);
    },
    p(o, a) {
      l = o, (!n || a & /*opened_folders*/
      128) && qt(e, "hidden", !/*opened_folders*/
      l[7].includes(
        /*i*/
        l[28]
      ));
    },
    i(o) {
      n || (J(t.$$.fragment, o), n = !0);
    },
    o(o) {
      te(t.$$.fragment, o), n = !1;
    },
    d(o) {
      o && Ee(e), nt(t), i = !1, ni(f);
    }
  };
}
function zt(l) {
  let e, t;
  function n(...s) {
    return (
      /*func_1*/
      l[17](
        /*name*/
        l[25],
        ...s
      )
    );
  }
  function i(...s) {
    return (
      /*func_3*/
      l[18](
        /*name*/
        l[25],
        ...s
      )
    );
  }
  function f(...s) {
    return (
      /*func_5*/
      l[19](
        /*name*/
        l[25],
        ...s
      )
    );
  }
  return e = new il({
    props: {
      path: [
        .../*path*/
        l[0],
        /*name*/
        l[25]
      ],
      all_files: (
        /*all_files*/
        l[1]
      ),
      selected_files: (
        /*selected_files*/
        l[2].filter(n).map(Lt)
      ),
      selected_folders: (
        /*selected_folders*/
        l[3].filter(i).map(Mt)
      ),
      is_selected_entirely: (
        /*selected_folders*/
        l[3].some(f)
      ),
      interactive: (
        /*interactive*/
        l[4]
      ),
      file_count: (
        /*file_count*/
        l[5]
      ),
      valid_for_selection: (
        /*valid*/
        l[26]
      )
    }
  }), e.$on(
    "check",
    /*check_handler*/
    l[20]
  ), {
    c() {
      lt(e.$$.fragment);
    },
    m(s, r) {
      it(e, s, r), t = !0;
    },
    p(s, r) {
      l = s;
      const o = {};
      r & /*path, content*/
      65 && (o.path = [
        .../*path*/
        l[0],
        /*name*/
        l[25]
      ]), r & /*all_files*/
      2 && (o.all_files = /*all_files*/
      l[1]), r & /*selected_files, content*/
      68 && (o.selected_files = /*selected_files*/
      l[2].filter(n).map(Lt)), r & /*selected_folders, content*/
      72 && (o.selected_folders = /*selected_folders*/
      l[3].filter(i).map(Mt)), r & /*selected_folders, content*/
      72 && (o.is_selected_entirely = /*selected_folders*/
      l[3].some(f)), r & /*interactive*/
      16 && (o.interactive = /*interactive*/
      l[4]), r & /*file_count*/
      32 && (o.file_count = /*file_count*/
      l[5]), r & /*content*/
      64 && (o.valid_for_selection = /*valid*/
      l[26]), e.$set(o);
    },
    i(s) {
      t || (J(e.$$.fragment, s), t = !0);
    },
    o(s) {
      te(e.$$.fragment, s), t = !1;
    },
    d(s) {
      nt(e, s);
    }
  };
}
function Ft(l) {
  let e, t, n, i, f, s, r, o = (
    /*name*/
    l[25] + ""
  ), a, c, _ = (
    /*type*/
    l[24] === "folder" && /*opened_folders*/
    l[7].includes(
      /*i*/
      l[28]
    )
  ), d, h;
  function g(...k) {
    return (
      /*func*/
      l[13](
        /*name*/
        l[25],
        ...k
      )
    );
  }
  function y(...k) {
    return (
      /*change_handler*/
      l[14](
        /*name*/
        l[25],
        /*type*/
        l[24],
        /*i*/
        l[28],
        ...k
      )
    );
  }
  n = new xn({
    props: {
      disabled: !/*interactive*/
      l[4] || /*type*/
      l[24] === "folder" && /*file_count*/
      l[5] === "single",
      value: (
        /*type*/
        (l[24] === "file" ? (
          /*selected_files*/
          l[2]
        ) : (
          /*selected_folders*/
          l[3]
        )).some(g)
      )
    }
  }), n.$on("change", y);
  const C = [ci, ai], z = [];
  function m(k, b) {
    return (
      /*type*/
      k[24] === "folder" ? 0 : 1
    );
  }
  f = m(l), s = z[f] = C[f](l);
  let u = _ && zt(l);
  return {
    c() {
      e = be("li"), t = be("span"), lt(n.$$.fragment), i = ze(), s.c(), r = ze(), a = fi(o), c = ze(), u && u.c(), d = ze(), Z(t, "class", "wrap svelte-zlvxd5"), Z(e, "class", "svelte-zlvxd5");
    },
    m(k, b) {
      De(k, e, b), oe(e, t), it(n, t, null), oe(t, i), z[f].m(t, null), oe(t, r), oe(t, a), oe(e, c), u && u.m(e, null), oe(e, d), h = !0;
    },
    p(k, b) {
      l = k;
      const w = {};
      b & /*interactive, content, file_count*/
      112 && (w.disabled = !/*interactive*/
      l[4] || /*type*/
      l[24] === "folder" && /*file_count*/
      l[5] === "single"), b & /*content, selected_files, selected_folders*/
      76 && (w.value = /*type*/
      (l[24] === "file" ? (
        /*selected_files*/
        l[2]
      ) : (
        /*selected_folders*/
        l[3]
      )).some(g)), n.$set(w);
      let V = f;
      f = m(l), f === V ? z[f].p(l, b) : (Qe(), te(z[V], 1, 1, () => {
        z[V] = null;
      }), Ke(), s = z[f], s ? s.p(l, b) : (s = z[f] = C[f](l), s.c()), J(s, 1), s.m(t, r)), (!h || b & /*content*/
      64) && o !== (o = /*name*/
      l[25] + "") && si(a, o), b & /*content, opened_folders*/
      192 && (_ = /*type*/
      l[24] === "folder" && /*opened_folders*/
      l[7].includes(
        /*i*/
        l[28]
      )), _ ? u ? (u.p(l, b), b & /*content, opened_folders*/
      192 && J(u, 1)) : (u = zt(l), u.c(), J(u, 1), u.m(e, d)) : u && (Qe(), te(u, 1, 1, () => {
        u = null;
      }), Ke());
    },
    i(k) {
      h || (J(n.$$.fragment, k), J(s), J(u), h = !0);
    },
    o(k) {
      te(n.$$.fragment, k), te(s), te(u), h = !1;
    },
    d(k) {
      k && Ee(e), nt(n), z[f].d(), u && u.d();
    }
  };
}
function _i(l) {
  let e, t, n = kt(
    /*content*/
    l[6]
  ), i = [];
  for (let s = 0; s < n.length; s += 1)
    i[s] = Ft(St(l, n, s));
  const f = (s) => te(i[s], 1, 1, () => {
    i[s] = null;
  });
  return {
    c() {
      e = be("ul");
      for (let s = 0; s < i.length; s += 1)
        i[s].c();
      Z(e, "class", "svelte-zlvxd5");
    },
    m(s, r) {
      De(s, e, r);
      for (let o = 0; o < i.length; o += 1)
        i[o] && i[o].m(e, null);
      t = !0;
    },
    p(s, [r]) {
      if (r & /*path, content, all_files, selected_files, selected_folders, interactive, file_count, opened_folders, toggle_open_folder, dispatch, open_folder*/
      2047) {
        n = kt(
          /*content*/
          s[6]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = St(s, n, o);
          i[o] ? (i[o].p(a, r), J(i[o], 1)) : (i[o] = Ft(a), i[o].c(), J(i[o], 1), i[o].m(e, null));
        }
        for (Qe(), o = n.length; o < i.length; o += 1)
          f(o);
        Ke();
      }
    },
    i(s) {
      if (!t) {
        for (let r = 0; r < n.length; r += 1)
          J(i[r]);
        t = !0;
      }
    },
    o(s) {
      i = i.filter(Boolean);
      for (let r = 0; r < i.length; r += 1)
        te(i[r]);
      t = !1;
    },
    d(s) {
      s && Ee(e), ti(i, s);
    }
  };
}
const Lt = (l) => l.slice(1), Mt = (l) => l.slice(1);
function ui(l, e, t) {
  let { path: n = [] } = e, { all_files: i = [] } = e, { selected_files: f = [] } = e, { selected_folders: s = [] } = e, { is_selected_entirely: r = !1 } = e, { interactive: o } = e, { file_count: a = "multiple" } = e, { valid_for_selection: c } = e, _ = [], d = [];
  const h = (p) => {
    d.includes(p) ? t(7, d = d.filter((L) => L !== p)) : t(7, d = [...d, p]);
  }, g = (p) => {
    d.includes(p) || t(7, d = [...d, p]);
  }, y = (p, L) => L.length === p.length - 1 ? L.join("/") === p.slice(0, L.length).join("/") : !1;
  function C(p, L) {
    let j = [];
    return p.length === 0 ? j = L.filter((I) => I.path.length === 1) : j = L.filter((I) => y(I.path, p)), c && (j = [{ name: ".", type: "file" }, ...j]), j;
  }
  function z(p) {
    return p.map((j, I) => j.type === "folder" && (r || f.some((Y) => Y[0] === j.name)) ? I : null).filter((j) => j !== null);
  }
  const m = ri(), u = (p, L) => L[0] === p && L.length === 1, k = (p, L, j, I) => {
    let Y = I.detail;
    m("check", { path: [...n, p], checked: Y, type: L }), L === "folder" && Y && g(j);
  }, b = (p) => h(p), w = (p, { key: L }) => {
    (L === " " || L === "Enter") && h(p);
  }, V = (p, L) => L[0] === p, U = (p, L) => L[0] === p, re = (p, L) => L[0] === p && L.length === 1;
  function $(p) {
    ei.call(this, l, p);
  }
  return l.$$set = (p) => {
    "path" in p && t(0, n = p.path), "all_files" in p && t(1, i = p.all_files), "selected_files" in p && t(2, f = p.selected_files), "selected_folders" in p && t(3, s = p.selected_folders), "is_selected_entirely" in p && t(11, r = p.is_selected_entirely), "interactive" in p && t(4, o = p.interactive), "file_count" in p && t(5, a = p.file_count), "valid_for_selection" in p && t(12, c = p.valid_for_selection);
  }, l.$$.update = () => {
    l.$$.dirty & /*path, all_files*/
    3 && t(6, _ = C(n, i)), l.$$.dirty & /*is_selected_entirely, content, path*/
    2113 && r && _.forEach((p) => {
      m("check", {
        path: [...n, p.name],
        checked: !0,
        type: p.type
      });
    }), l.$$.dirty & /*content*/
    64 && t(7, d = z(_));
  }, [
    n,
    i,
    f,
    s,
    o,
    a,
    _,
    d,
    h,
    g,
    m,
    r,
    c,
    u,
    k,
    b,
    w,
    V,
    U,
    re,
    $
  ];
}
class il extends $n {
  constructor(e) {
    super(), li(this, e, ui, _i, ii, {
      path: 0,
      all_files: 1,
      selected_files: 2,
      selected_folders: 3,
      is_selected_entirely: 11,
      interactive: 4,
      file_count: 5,
      valid_for_selection: 12
    });
  }
}
const {
  SvelteComponent: di,
  attr: mi,
  create_component: hi,
  destroy_component: gi,
  detach: bi,
  element: pi,
  init: wi,
  insert: ki,
  mount_component: vi,
  safe_not_equal: yi,
  transition_in: Ci,
  transition_out: qi
} = window.__gradio__svelte__internal;
function Si(l) {
  let e, t, n;
  return t = new il({
    props: {
      path: [],
      all_files: (
        /*all_files*/
        l[4]
      ),
      selected_files: (
        /*selected_files*/
        l[3]
      ),
      selected_folders: (
        /*selected_folders*/
        l[2]
      ),
      interactive: (
        /*interactive*/
        l[0]
      ),
      file_count: (
        /*file_count*/
        l[1]
      ),
      valid_for_selection: !1
    }
  }), t.$on(
    "check",
    /*check_handler*/
    l[10]
  ), {
    c() {
      e = pi("div"), hi(t.$$.fragment), mi(e, "class", "file-wrap svelte-h8i5yo");
    },
    m(i, f) {
      ki(i, e, f), vi(t, e, null), n = !0;
    },
    p(i, [f]) {
      const s = {};
      f & /*all_files*/
      16 && (s.all_files = /*all_files*/
      i[4]), f & /*selected_files*/
      8 && (s.selected_files = /*selected_files*/
      i[3]), f & /*selected_folders*/
      4 && (s.selected_folders = /*selected_folders*/
      i[2]), f & /*interactive*/
      1 && (s.interactive = /*interactive*/
      i[0]), f & /*file_count*/
      2 && (s.file_count = /*file_count*/
      i[1]), t.$set(s);
    },
    i(i) {
      n || (Ci(t.$$.fragment, i), n = !0);
    },
    o(i) {
      qi(t.$$.fragment, i), n = !1;
    },
    d(i) {
      i && bi(e), gi(t);
    }
  };
}
function zi(l) {
  const e = l.split("/").filter((n) => n.trim().length > 0), t = !l.endsWith("/");
  return {
    name: e[e.length - 1],
    type: t ? "file" : "folder",
    path: e,
    valid: t
    // allow selection
  };
}
function Fi(l) {
  return l[0].map((n) => zi(n));
}
function Li(l) {
  return l.map((n) => n.split("/").filter((i) => i.trim().length > 0));
}
function Mi(l, e, t) {
  let n, { interactive: i } = e, { file_count: f = "multiple" } = e, { value: s = [] } = e, r = [], o = [];
  const a = (g, y) => g.join("/") === y.join("/"), c = (g, y) => y.some((C) => a(C, g)), _ = (g, y) => g.join("/").startsWith(y.join("/"));
  function d(g) {
    const y = g.map((z) => z.join("/")), C = s[0];
    t(9, s = [C, y]);
  }
  const h = (g) => {
    const { path: y, checked: C, type: z } = g.detail;
    C ? f === "single" ? d([y]) : z === "folder" ? c(y, r) || t(2, r = [...r, y]) : c(y, o) || d([...o, y]) : (t(2, r = r.filter((m) => !_(y, m))), z === "folder" ? (t(2, r = r.filter((m) => !_(m, y))), d(o.filter((m) => !_(m, y)))) : d(o.filter((m) => !a(m, y))));
  };
  return l.$$set = (g) => {
    "interactive" in g && t(0, i = g.interactive), "file_count" in g && t(1, f = g.file_count), "value" in g && t(9, s = g.value);
  }, l.$$.update = () => {
    l.$$.dirty & /*value*/
    512 && t(3, o = Li(s[1])), l.$$.dirty & /*value*/
    512 && t(4, n = Fi(s));
  }, [
    i,
    f,
    r,
    o,
    n,
    a,
    c,
    _,
    d,
    s,
    h
  ];
}
class Vi extends di {
  constructor(e) {
    super(), wi(this, e, Mi, Si, yi, { interactive: 0, file_count: 1, value: 9 });
  }
}
function de(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
function Me() {
}
function ji(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const sl = typeof window < "u";
let Vt = sl ? () => window.performance.now() : () => Date.now(), ol = sl ? (l) => requestAnimationFrame(l) : Me;
const ge = /* @__PURE__ */ new Set();
function fl(l) {
  ge.forEach((e) => {
    e.c(l) || (ge.delete(e), e.f());
  }), ge.size !== 0 && ol(fl);
}
function Ii(l) {
  let e;
  return ge.size === 0 && ol(fl), {
    promise: new Promise((t) => {
      ge.add(e = { c: l, f: t });
    }),
    abort() {
      ge.delete(e);
    }
  };
}
const ue = [];
function Ni(l, e = Me) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (ji(l, r) && (l = r, t)) {
      const o = !ue.length;
      for (const a of n)
        a[1](), ue.push(a, l);
      if (o) {
        for (let a = 0; a < ue.length; a += 2)
          ue[a][0](ue[a + 1]);
        ue.length = 0;
      }
    }
  }
  function f(r) {
    i(r(l));
  }
  function s(r, o = Me) {
    const a = [r, o];
    return n.add(a), n.size === 1 && (t = e(i, f) || Me), r(l), () => {
      n.delete(a), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: f, subscribe: s };
}
function jt(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function xe(l, e, t, n) {
  if (typeof t == "number" || jt(t)) {
    const i = n - t, f = (t - e) / (l.dt || 1 / 60), s = l.opts.stiffness * i, r = l.opts.damping * f, o = (s - r) * l.inv_mass, a = (f + o) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, jt(t) ? new Date(t.getTime() + a) : t + a);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, f) => xe(l, e[f], t[f], n[f])
      );
    if (typeof t == "object") {
      const i = {};
      for (const f in t)
        i[f] = xe(l, e[f], t[f], n[f]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function It(l, e = {}) {
  const t = Ni(l), { stiffness: n = 0.15, damping: i = 0.8, precision: f = 0.01 } = e;
  let s, r, o, a = l, c = l, _ = 1, d = 0, h = !1;
  function g(C, z = {}) {
    c = C;
    const m = o = {};
    return l == null || z.hard || y.stiffness >= 1 && y.damping >= 1 ? (h = !0, s = Vt(), a = C, t.set(l = c), Promise.resolve()) : (z.soft && (d = 1 / ((z.soft === !0 ? 0.5 : +z.soft) * 60), _ = 0), r || (s = Vt(), h = !1, r = Ii((u) => {
      if (h)
        return h = !1, r = null, !1;
      _ = Math.min(_ + d, 1);
      const k = {
        inv_mass: _,
        opts: y,
        settled: !0,
        dt: (u - s) * 60 / 1e3
      }, b = xe(k, a, l, c);
      return s = u, a = l, t.set(l = b), k.settled && (r = null), !k.settled;
    })), new Promise((u) => {
      r.promise.then(() => {
        m === o && u();
      });
    }));
  }
  const y = {
    set: g,
    update: (C, z) => g(C(c, l), z),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: f
  };
  return y;
}
const {
  SvelteComponent: Ei,
  append: O,
  attr: F,
  component_subscribe: Nt,
  detach: Di,
  element: Bi,
  init: Pi,
  insert: Zi,
  noop: Et,
  safe_not_equal: Gi,
  set_style: Fe,
  svg_element: H,
  toggle_class: Dt
} = window.__gradio__svelte__internal, { onMount: Ti } = window.__gradio__svelte__internal;
function Ui(l) {
  let e, t, n, i, f, s, r, o, a, c, _, d;
  return {
    c() {
      e = Bi("div"), t = H("svg"), n = H("g"), i = H("path"), f = H("path"), s = H("path"), r = H("path"), o = H("g"), a = H("path"), c = H("path"), _ = H("path"), d = H("path"), F(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), F(i, "fill", "#FF7C00"), F(i, "fill-opacity", "0.4"), F(i, "class", "svelte-43sxxs"), F(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), F(f, "fill", "#FF7C00"), F(f, "class", "svelte-43sxxs"), F(s, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), F(s, "fill", "#FF7C00"), F(s, "fill-opacity", "0.4"), F(s, "class", "svelte-43sxxs"), F(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), F(r, "fill", "#FF7C00"), F(r, "class", "svelte-43sxxs"), Fe(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), F(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), F(a, "fill", "#FF7C00"), F(a, "fill-opacity", "0.4"), F(a, "class", "svelte-43sxxs"), F(c, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), F(c, "fill", "#FF7C00"), F(c, "class", "svelte-43sxxs"), F(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), F(_, "fill", "#FF7C00"), F(_, "fill-opacity", "0.4"), F(_, "class", "svelte-43sxxs"), F(d, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), F(d, "fill", "#FF7C00"), F(d, "class", "svelte-43sxxs"), Fe(o, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), F(t, "viewBox", "-1200 -1200 3000 3000"), F(t, "fill", "none"), F(t, "xmlns", "http://www.w3.org/2000/svg"), F(t, "class", "svelte-43sxxs"), F(e, "class", "svelte-43sxxs"), Dt(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(h, g) {
      Zi(h, e, g), O(e, t), O(t, n), O(n, i), O(n, f), O(n, s), O(n, r), O(t, o), O(o, a), O(o, c), O(o, _), O(o, d);
    },
    p(h, [g]) {
      g & /*$top*/
      2 && Fe(n, "transform", "translate(" + /*$top*/
      h[1][0] + "px, " + /*$top*/
      h[1][1] + "px)"), g & /*$bottom*/
      4 && Fe(o, "transform", "translate(" + /*$bottom*/
      h[2][0] + "px, " + /*$bottom*/
      h[2][1] + "px)"), g & /*margin*/
      1 && Dt(
        e,
        "margin",
        /*margin*/
        h[0]
      );
    },
    i: Et,
    o: Et,
    d(h) {
      h && Di(e);
    }
  };
}
function Ai(l, e, t) {
  let n, i;
  var f = this && this.__awaiter || function(h, g, y, C) {
    function z(m) {
      return m instanceof y ? m : new y(function(u) {
        u(m);
      });
    }
    return new (y || (y = Promise))(function(m, u) {
      function k(V) {
        try {
          w(C.next(V));
        } catch (U) {
          u(U);
        }
      }
      function b(V) {
        try {
          w(C.throw(V));
        } catch (U) {
          u(U);
        }
      }
      function w(V) {
        V.done ? m(V.value) : z(V.value).then(k, b);
      }
      w((C = C.apply(h, g || [])).next());
    });
  };
  let { margin: s = !0 } = e;
  const r = It([0, 0]);
  Nt(l, r, (h) => t(1, n = h));
  const o = It([0, 0]);
  Nt(l, o, (h) => t(2, i = h));
  let a;
  function c() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 140]), o.set([-125, -140])]), yield Promise.all([r.set([-125, 140]), o.set([125, -140])]), yield Promise.all([r.set([-125, 0]), o.set([125, -0])]), yield Promise.all([r.set([125, 0]), o.set([-125, 0])]);
    });
  }
  function _() {
    return f(this, void 0, void 0, function* () {
      yield c(), a || _();
    });
  }
  function d() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 0]), o.set([-125, 0])]), _();
    });
  }
  return Ti(() => (d(), () => a = !0)), l.$$set = (h) => {
    "margin" in h && t(0, s = h.margin);
  }, [s, n, i, r, o];
}
class Oi extends Ei {
  constructor(e) {
    super(), Pi(this, e, Ai, Ui, Gi, { margin: 0 });
  }
}
const {
  SvelteComponent: Hi,
  append: fe,
  attr: X,
  binding_callbacks: Bt,
  check_outros: $e,
  create_component: rl,
  create_slot: al,
  destroy_component: cl,
  destroy_each: _l,
  detach: q,
  element: Q,
  empty: pe,
  ensure_array_like: Ve,
  get_all_dirty_from_scope: ul,
  get_slot_changes: dl,
  group_outros: et,
  init: Ji,
  insert: S,
  mount_component: ml,
  noop: tt,
  safe_not_equal: Wi,
  set_data: T,
  set_style: ie,
  space: G,
  text: M,
  toggle_class: P,
  transition_in: W,
  transition_out: x,
  update_slot_base: hl
} = window.__gradio__svelte__internal, { tick: Xi } = window.__gradio__svelte__internal, { onDestroy: Yi } = window.__gradio__svelte__internal, { createEventDispatcher: Ri } = window.__gradio__svelte__internal, Ki = (l) => ({}), Pt = (l) => ({}), Qi = (l) => ({}), Zt = (l) => ({});
function Gt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function Tt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function xi(l) {
  let e, t, n, i, f = (
    /*i18n*/
    l[1]("common.error") + ""
  ), s, r, o;
  t = new Nn({
    props: {
      Icon: jl,
      label: (
        /*i18n*/
        l[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    l[32]
  );
  const a = (
    /*#slots*/
    l[30].error
  ), c = al(
    a,
    l,
    /*$$scope*/
    l[29],
    Pt
  );
  return {
    c() {
      e = Q("div"), rl(t.$$.fragment), n = G(), i = Q("span"), s = M(f), r = G(), c && c.c(), X(e, "class", "clear-status svelte-vopvsi"), X(i, "class", "error svelte-vopvsi");
    },
    m(_, d) {
      S(_, e, d), ml(t, e, null), S(_, n, d), S(_, i, d), fe(i, s), S(_, r, d), c && c.m(_, d), o = !0;
    },
    p(_, d) {
      const h = {};
      d[0] & /*i18n*/
      2 && (h.label = /*i18n*/
      _[1]("common.clear")), t.$set(h), (!o || d[0] & /*i18n*/
      2) && f !== (f = /*i18n*/
      _[1]("common.error") + "") && T(s, f), c && c.p && (!o || d[0] & /*$$scope*/
      536870912) && hl(
        c,
        a,
        _,
        /*$$scope*/
        _[29],
        o ? dl(
          a,
          /*$$scope*/
          _[29],
          d,
          Ki
        ) : ul(
          /*$$scope*/
          _[29]
        ),
        Pt
      );
    },
    i(_) {
      o || (W(t.$$.fragment, _), W(c, _), o = !0);
    },
    o(_) {
      x(t.$$.fragment, _), x(c, _), o = !1;
    },
    d(_) {
      _ && (q(e), q(n), q(i), q(r)), cl(t), c && c.d(_);
    }
  };
}
function $i(l) {
  let e, t, n, i, f, s, r, o, a, c = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ut(l)
  );
  function _(u, k) {
    if (
      /*progress*/
      u[7]
    )
      return ls;
    if (
      /*queue_position*/
      u[2] !== null && /*queue_size*/
      u[3] !== void 0 && /*queue_position*/
      u[2] >= 0
    )
      return ts;
    if (
      /*queue_position*/
      u[2] === 0
    )
      return es;
  }
  let d = _(l), h = d && d(l), g = (
    /*timer*/
    l[5] && Ht(l)
  );
  const y = [os, ss], C = [];
  function z(u, k) {
    return (
      /*last_progress_level*/
      u[15] != null ? 0 : (
        /*show_progress*/
        u[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = z(l)) && (s = C[f] = y[f](l));
  let m = !/*timer*/
  l[5] && Qt(l);
  return {
    c() {
      c && c.c(), e = G(), t = Q("div"), h && h.c(), n = G(), g && g.c(), i = G(), s && s.c(), r = G(), m && m.c(), o = pe(), X(t, "class", "progress-text svelte-vopvsi"), P(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), P(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(u, k) {
      c && c.m(u, k), S(u, e, k), S(u, t, k), h && h.m(t, null), fe(t, n), g && g.m(t, null), S(u, i, k), ~f && C[f].m(u, k), S(u, r, k), m && m.m(u, k), S(u, o, k), a = !0;
    },
    p(u, k) {
      /*variant*/
      u[8] === "default" && /*show_eta_bar*/
      u[18] && /*show_progress*/
      u[6] === "full" ? c ? c.p(u, k) : (c = Ut(u), c.c(), c.m(e.parentNode, e)) : c && (c.d(1), c = null), d === (d = _(u)) && h ? h.p(u, k) : (h && h.d(1), h = d && d(u), h && (h.c(), h.m(t, n))), /*timer*/
      u[5] ? g ? g.p(u, k) : (g = Ht(u), g.c(), g.m(t, null)) : g && (g.d(1), g = null), (!a || k[0] & /*variant*/
      256) && P(
        t,
        "meta-text-center",
        /*variant*/
        u[8] === "center"
      ), (!a || k[0] & /*variant*/
      256) && P(
        t,
        "meta-text",
        /*variant*/
        u[8] === "default"
      );
      let b = f;
      f = z(u), f === b ? ~f && C[f].p(u, k) : (s && (et(), x(C[b], 1, 1, () => {
        C[b] = null;
      }), $e()), ~f ? (s = C[f], s ? s.p(u, k) : (s = C[f] = y[f](u), s.c()), W(s, 1), s.m(r.parentNode, r)) : s = null), /*timer*/
      u[5] ? m && (et(), x(m, 1, 1, () => {
        m = null;
      }), $e()) : m ? (m.p(u, k), k[0] & /*timer*/
      32 && W(m, 1)) : (m = Qt(u), m.c(), W(m, 1), m.m(o.parentNode, o));
    },
    i(u) {
      a || (W(s), W(m), a = !0);
    },
    o(u) {
      x(s), x(m), a = !1;
    },
    d(u) {
      u && (q(e), q(t), q(i), q(r), q(o)), c && c.d(u), h && h.d(), g && g.d(), ~f && C[f].d(u), m && m.d(u);
    }
  };
}
function Ut(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = Q("div"), X(e, "class", "eta-bar svelte-vopvsi"), ie(e, "transform", t);
    },
    m(n, i) {
      S(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && ie(e, "transform", t);
    },
    d(n) {
      n && q(e);
    }
  };
}
function es(l) {
  let e;
  return {
    c() {
      e = M("processing |");
    },
    m(t, n) {
      S(t, e, n);
    },
    p: tt,
    d(t) {
      t && q(e);
    }
  };
}
function ts(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, f, s;
  return {
    c() {
      e = M("queue: "), n = M(t), i = M("/"), f = M(
        /*queue_size*/
        l[3]
      ), s = M(" |");
    },
    m(r, o) {
      S(r, e, o), S(r, n, o), S(r, i, o), S(r, f, o), S(r, s, o);
    },
    p(r, o) {
      o[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && T(n, t), o[0] & /*queue_size*/
      8 && T(
        f,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (q(e), q(n), q(i), q(f), q(s));
    }
  };
}
function ls(l) {
  let e, t = Ve(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Ot(Tt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = pe();
    },
    m(i, f) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, f);
      S(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress*/
      128) {
        t = Ve(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const r = Tt(i, t, s);
          n[s] ? n[s].p(r, f) : (n[s] = Ot(r), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && q(e), _l(n, i);
    }
  };
}
function At(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, i, f = " ", s;
  function r(c, _) {
    return (
      /*p*/
      c[41].length != null ? is : ns
    );
  }
  let o = r(l), a = o(l);
  return {
    c() {
      a.c(), e = G(), n = M(t), i = M(" | "), s = M(f);
    },
    m(c, _) {
      a.m(c, _), S(c, e, _), S(c, n, _), S(c, i, _), S(c, s, _);
    },
    p(c, _) {
      o === (o = r(c)) && a ? a.p(c, _) : (a.d(1), a = o(c), a && (a.c(), a.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      c[41].unit + "") && T(n, t);
    },
    d(c) {
      c && (q(e), q(n), q(i), q(s)), a.d(c);
    }
  };
}
function ns(l) {
  let e = de(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = M(e);
    },
    m(n, i) {
      S(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = de(
        /*p*/
        n[41].index || 0
      ) + "") && T(t, e);
    },
    d(n) {
      n && q(t);
    }
  };
}
function is(l) {
  let e = de(
    /*p*/
    l[41].index || 0
  ) + "", t, n, i = de(
    /*p*/
    l[41].length
  ) + "", f;
  return {
    c() {
      t = M(e), n = M("/"), f = M(i);
    },
    m(s, r) {
      S(s, t, r), S(s, n, r), S(s, f, r);
    },
    p(s, r) {
      r[0] & /*progress*/
      128 && e !== (e = de(
        /*p*/
        s[41].index || 0
      ) + "") && T(t, e), r[0] & /*progress*/
      128 && i !== (i = de(
        /*p*/
        s[41].length
      ) + "") && T(f, i);
    },
    d(s) {
      s && (q(t), q(n), q(f));
    }
  };
}
function Ot(l) {
  let e, t = (
    /*p*/
    l[41].index != null && At(l)
  );
  return {
    c() {
      t && t.c(), e = pe();
    },
    m(n, i) {
      t && t.m(n, i), S(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? t ? t.p(n, i) : (t = At(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && q(e), t && t.d(n);
    }
  };
}
function Ht(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = M(
        /*formatted_timer*/
        l[20]
      ), n = M(t), i = M("s");
    },
    m(f, s) {
      S(f, e, s), S(f, n, s), S(f, i, s);
    },
    p(f, s) {
      s[0] & /*formatted_timer*/
      1048576 && T(
        e,
        /*formatted_timer*/
        f[20]
      ), s[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && T(n, t);
    },
    d(f) {
      f && (q(e), q(n), q(i));
    }
  };
}
function ss(l) {
  let e, t;
  return e = new Oi({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      rl(e.$$.fragment);
    },
    m(n, i) {
      ml(e, n, i), t = !0;
    },
    p(n, i) {
      const f = {};
      i[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), e.$set(f);
    },
    i(n) {
      t || (W(e.$$.fragment, n), t = !0);
    },
    o(n) {
      x(e.$$.fragment, n), t = !1;
    },
    d(n) {
      cl(e, n);
    }
  };
}
function os(l) {
  let e, t, n, i, f, s = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && Jt(l)
  );
  return {
    c() {
      e = Q("div"), t = Q("div"), r && r.c(), n = G(), i = Q("div"), f = Q("div"), X(t, "class", "progress-level-inner svelte-vopvsi"), X(f, "class", "progress-bar svelte-vopvsi"), ie(f, "width", s), X(i, "class", "progress-bar-wrap svelte-vopvsi"), X(e, "class", "progress-level svelte-vopvsi");
    },
    m(o, a) {
      S(o, e, a), fe(e, t), r && r.m(t, null), fe(e, n), fe(e, i), fe(i, f), l[31](f);
    },
    p(o, a) {
      /*progress*/
      o[7] != null ? r ? r.p(o, a) : (r = Jt(o), r.c(), r.m(t, null)) : r && (r.d(1), r = null), a[0] & /*last_progress_level*/
      32768 && s !== (s = `${/*last_progress_level*/
      o[15] * 100}%`) && ie(f, "width", s);
    },
    i: tt,
    o: tt,
    d(o) {
      o && q(e), r && r.d(), l[31](null);
    }
  };
}
function Jt(l) {
  let e, t = Ve(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Kt(Gt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = pe();
    },
    m(i, f) {
      for (let s = 0; s < n.length; s += 1)
        n[s] && n[s].m(i, f);
      S(i, e, f);
    },
    p(i, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        t = Ve(
          /*progress*/
          i[7]
        );
        let s;
        for (s = 0; s < t.length; s += 1) {
          const r = Gt(i, t, s);
          n[s] ? n[s].p(r, f) : (n[s] = Kt(r), n[s].c(), n[s].m(e.parentNode, e));
        }
        for (; s < n.length; s += 1)
          n[s].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && q(e), _l(n, i);
    }
  };
}
function Wt(l) {
  let e, t, n, i, f = (
    /*i*/
    l[43] !== 0 && fs()
  ), s = (
    /*p*/
    l[41].desc != null && Xt(l)
  ), r = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && Yt()
  ), o = (
    /*progress_level*/
    l[14] != null && Rt(l)
  );
  return {
    c() {
      f && f.c(), e = G(), s && s.c(), t = G(), r && r.c(), n = G(), o && o.c(), i = pe();
    },
    m(a, c) {
      f && f.m(a, c), S(a, e, c), s && s.m(a, c), S(a, t, c), r && r.m(a, c), S(a, n, c), o && o.m(a, c), S(a, i, c);
    },
    p(a, c) {
      /*p*/
      a[41].desc != null ? s ? s.p(a, c) : (s = Xt(a), s.c(), s.m(t.parentNode, t)) : s && (s.d(1), s = null), /*p*/
      a[41].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[43]
      ] != null ? r || (r = Yt(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      a[14] != null ? o ? o.p(a, c) : (o = Rt(a), o.c(), o.m(i.parentNode, i)) : o && (o.d(1), o = null);
    },
    d(a) {
      a && (q(e), q(t), q(n), q(i)), f && f.d(a), s && s.d(a), r && r.d(a), o && o.d(a);
    }
  };
}
function fs(l) {
  let e;
  return {
    c() {
      e = M(" /");
    },
    m(t, n) {
      S(t, e, n);
    },
    d(t) {
      t && q(e);
    }
  };
}
function Xt(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = M(e);
    },
    m(n, i) {
      S(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && T(t, e);
    },
    d(n) {
      n && q(t);
    }
  };
}
function Yt(l) {
  let e;
  return {
    c() {
      e = M("-");
    },
    m(t, n) {
      S(t, e, n);
    },
    d(t) {
      t && q(e);
    }
  };
}
function Rt(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = M(e), n = M("%");
    },
    m(i, f) {
      S(i, t, f), S(i, n, f);
    },
    p(i, f) {
      f[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && T(t, e);
    },
    d(i) {
      i && (q(t), q(n));
    }
  };
}
function Kt(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && Wt(l)
  );
  return {
    c() {
      t && t.c(), e = pe();
    },
    m(n, i) {
      t && t.m(n, i), S(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, i) : (t = Wt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && q(e), t && t.d(n);
    }
  };
}
function Qt(l) {
  let e, t, n, i;
  const f = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), s = al(
    f,
    l,
    /*$$scope*/
    l[29],
    Zt
  );
  return {
    c() {
      e = Q("p"), t = M(
        /*loading_text*/
        l[9]
      ), n = G(), s && s.c(), X(e, "class", "loading svelte-vopvsi");
    },
    m(r, o) {
      S(r, e, o), fe(e, t), S(r, n, o), s && s.m(r, o), i = !0;
    },
    p(r, o) {
      (!i || o[0] & /*loading_text*/
      512) && T(
        t,
        /*loading_text*/
        r[9]
      ), s && s.p && (!i || o[0] & /*$$scope*/
      536870912) && hl(
        s,
        f,
        r,
        /*$$scope*/
        r[29],
        i ? dl(
          f,
          /*$$scope*/
          r[29],
          o,
          Qi
        ) : ul(
          /*$$scope*/
          r[29]
        ),
        Zt
      );
    },
    i(r) {
      i || (W(s, r), i = !0);
    },
    o(r) {
      x(s, r), i = !1;
    },
    d(r) {
      r && (q(e), q(n)), s && s.d(r);
    }
  };
}
function rs(l) {
  let e, t, n, i, f;
  const s = [$i, xi], r = [];
  function o(a, c) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = o(l)) && (n = r[t] = s[t](l)), {
    c() {
      e = Q("div"), n && n.c(), X(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-vopvsi"), P(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), P(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), P(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), P(
        e,
        "border",
        /*border*/
        l[12]
      ), ie(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), ie(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, c) {
      S(a, e, c), ~t && r[t].m(e, null), l[33](e), f = !0;
    },
    p(a, c) {
      let _ = t;
      t = o(a), t === _ ? ~t && r[t].p(a, c) : (n && (et(), x(r[_], 1, 1, () => {
        r[_] = null;
      }), $e()), ~t ? (n = r[t], n ? n.p(a, c) : (n = r[t] = s[t](a), n.c()), W(n, 1), n.m(e, null)) : n = null), (!f || c[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-vopvsi")) && X(e, "class", i), (!f || c[0] & /*variant, show_progress, status, show_progress*/
      336) && P(e, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || c[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && P(
        e,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || c[0] & /*variant, show_progress, status*/
      336) && P(
        e,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || c[0] & /*variant, show_progress, border*/
      4416) && P(
        e,
        "border",
        /*border*/
        a[12]
      ), c[0] & /*absolute*/
      1024 && ie(
        e,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), c[0] & /*absolute*/
      1024 && ie(
        e,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      f || (W(n), f = !0);
    },
    o(a) {
      x(n), f = !1;
    },
    d(a) {
      a && q(e), ~t && r[t].d(), l[33](null);
    }
  };
}
var as = function(l, e, t, n) {
  function i(f) {
    return f instanceof t ? f : new t(function(s) {
      s(f);
    });
  }
  return new (t || (t = Promise))(function(f, s) {
    function r(c) {
      try {
        a(n.next(c));
      } catch (_) {
        s(_);
      }
    }
    function o(c) {
      try {
        a(n.throw(c));
      } catch (_) {
        s(_);
      }
    }
    function a(c) {
      c.done ? f(c.value) : i(c.value).then(r, o);
    }
    a((n = n.apply(l, e || [])).next());
  });
};
let Le = [], Je = !1;
function cs(l) {
  return as(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Le.push(e), !Je)
        Je = !0;
      else
        return;
      yield Xi(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < Le.length; i++) {
          const s = Le[i].getBoundingClientRect();
          (i === 0 || s.top + window.scrollY <= n[0]) && (n[0] = s.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Je = !1, Le = [];
      });
    }
  });
}
function _s(l, e, t) {
  let n, { $$slots: i = {}, $$scope: f } = e;
  this && this.__awaiter;
  const s = Ri();
  let { i18n: r } = e, { eta: o = null } = e, { queue_position: a } = e, { queue_size: c } = e, { status: _ } = e, { scroll_to_output: d = !1 } = e, { timer: h = !0 } = e, { show_progress: g = "full" } = e, { message: y = null } = e, { progress: C = null } = e, { variant: z = "default" } = e, { loading_text: m = "Loading..." } = e, { absolute: u = !0 } = e, { translucent: k = !1 } = e, { border: b = !1 } = e, { autoscroll: w } = e, V, U = !1, re = 0, $ = 0, p = null, L = null, j = 0, I = null, Y, le = null, st = !0;
  const bl = () => {
    t(0, o = t(27, p = t(19, ke = null))), t(25, re = performance.now()), t(26, $ = 0), U = !0, ot();
  };
  function ot() {
    requestAnimationFrame(() => {
      t(26, $ = (performance.now() - re) / 1e3), U && ot();
    });
  }
  function ft() {
    t(26, $ = 0), t(0, o = t(27, p = t(19, ke = null))), U && (U = !1);
  }
  Yi(() => {
    U && ft();
  });
  let ke = null;
  function pl(v) {
    Bt[v ? "unshift" : "push"](() => {
      le = v, t(16, le), t(7, C), t(14, I), t(15, Y);
    });
  }
  const wl = () => {
    s("clear_status");
  };
  function kl(v) {
    Bt[v ? "unshift" : "push"](() => {
      V = v, t(13, V);
    });
  }
  return l.$$set = (v) => {
    "i18n" in v && t(1, r = v.i18n), "eta" in v && t(0, o = v.eta), "queue_position" in v && t(2, a = v.queue_position), "queue_size" in v && t(3, c = v.queue_size), "status" in v && t(4, _ = v.status), "scroll_to_output" in v && t(22, d = v.scroll_to_output), "timer" in v && t(5, h = v.timer), "show_progress" in v && t(6, g = v.show_progress), "message" in v && t(23, y = v.message), "progress" in v && t(7, C = v.progress), "variant" in v && t(8, z = v.variant), "loading_text" in v && t(9, m = v.loading_text), "absolute" in v && t(10, u = v.absolute), "translucent" in v && t(11, k = v.translucent), "border" in v && t(12, b = v.border), "autoscroll" in v && t(24, w = v.autoscroll), "$$scope" in v && t(29, f = v.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (o === null && t(0, o = p), o != null && p !== o && (t(28, L = (performance.now() - re) / 1e3 + o), t(19, ke = L.toFixed(1)), t(27, p = o))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, j = L === null || L <= 0 || !$ ? null : Math.min($ / L, 1)), l.$$.dirty[0] & /*progress*/
    128 && C != null && t(18, st = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (C != null ? t(14, I = C.map((v) => {
      if (v.index != null && v.length != null)
        return v.index / v.length;
      if (v.progress != null)
        return v.progress;
    })) : t(14, I = null), I ? (t(15, Y = I[I.length - 1]), le && (Y === 0 ? t(16, le.style.transition = "0", le) : t(16, le.style.transition = "150ms", le))) : t(15, Y = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? bl() : ft()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && V && d && (_ === "pending" || _ === "complete") && cs(V, w), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = $.toFixed(1));
  }, [
    o,
    r,
    a,
    c,
    _,
    h,
    g,
    C,
    z,
    m,
    u,
    k,
    b,
    V,
    I,
    Y,
    le,
    j,
    st,
    ke,
    n,
    s,
    d,
    y,
    w,
    re,
    $,
    p,
    L,
    f,
    i,
    pl,
    wl,
    kl
  ];
}
class us extends Hi {
  constructor(e) {
    super(), Ji(
      this,
      e,
      _s,
      rs,
      Wi,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: ds,
  add_flush_callback: ms,
  assign: hs,
  bind: gs,
  binding_callbacks: bs,
  check_outros: ps,
  create_component: je,
  destroy_component: Ie,
  detach: We,
  empty: ws,
  flush: E,
  get_spread_object: ks,
  get_spread_update: vs,
  group_outros: ys,
  init: Cs,
  insert: Xe,
  mount_component: Ne,
  noop: qs,
  safe_not_equal: gl,
  space: xt,
  transition_in: me,
  transition_out: he
} = window.__gradio__svelte__internal;
function $t(l) {
  let e, t, n;
  function i(s) {
    l[17](s);
  }
  let f = {
    file_count: (
      /*file_count*/
      l[7]
    ),
    interactive: (
      /*interactive*/
      l[13]
    )
  };
  return (
    /*value*/
    l[0] !== void 0 && (f.value = /*value*/
    l[0]), e = new Vi({ props: f }), bs.push(() => gs(e, "value", i)), {
      c() {
        je(e.$$.fragment);
      },
      m(s, r) {
        Ne(e, s, r), n = !0;
      },
      p(s, r) {
        const o = {};
        r & /*file_count*/
        128 && (o.file_count = /*file_count*/
        s[7]), r & /*interactive*/
        8192 && (o.interactive = /*interactive*/
        s[13]), !t && r & /*value*/
        1 && (t = !0, o.value = /*value*/
        s[0], ms(() => t = !1)), e.$set(o);
      },
      i(s) {
        n || (me(e.$$.fragment, s), n = !0);
      },
      o(s) {
        he(e.$$.fragment, s), n = !1;
      },
      d(s) {
        Ie(e, s);
      }
    }
  );
}
function Ss(l) {
  let e, t, n, i, f = (
    /*rerender_key*/
    l[14]
  ), s, r;
  const o = [
    /*loading_status*/
    l[8],
    {
      autoscroll: (
        /*gradio*/
        l[12].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      l[12].i18n
    ) }
  ];
  let a = {};
  for (let _ = 0; _ < o.length; _ += 1)
    a = hs(a, o[_]);
  e = new us({ props: a }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[16]
  ), n = new bn({
    props: {
      show_label: (
        /*show_label*/
        l[5]
      ),
      Icon: Zl,
      label: (
        /*label*/
        l[4] || "FileExplorer"
      ),
      float: !1
    }
  });
  let c = $t(l);
  return {
    c() {
      je(e.$$.fragment), t = xt(), je(n.$$.fragment), i = xt(), c.c(), s = ws();
    },
    m(_, d) {
      Ne(e, _, d), Xe(_, t, d), Ne(n, _, d), Xe(_, i, d), c.m(_, d), Xe(_, s, d), r = !0;
    },
    p(_, d) {
      const h = d & /*loading_status, gradio*/
      4352 ? vs(o, [
        d & /*loading_status*/
        256 && ks(
          /*loading_status*/
          _[8]
        ),
        d & /*gradio*/
        4096 && {
          autoscroll: (
            /*gradio*/
            _[12].autoscroll
          )
        },
        d & /*gradio*/
        4096 && { i18n: (
          /*gradio*/
          _[12].i18n
        ) }
      ]) : {};
      e.$set(h);
      const g = {};
      d & /*show_label*/
      32 && (g.show_label = /*show_label*/
      _[5]), d & /*label*/
      16 && (g.label = /*label*/
      _[4] || "FileExplorer"), n.$set(g), d & /*rerender_key*/
      16384 && gl(f, f = /*rerender_key*/
      _[14]) ? (ys(), he(c, 1, 1, qs), ps(), c = $t(_), c.c(), me(c, 1), c.m(s.parentNode, s)) : c.p(_, d);
    },
    i(_) {
      r || (me(e.$$.fragment, _), me(n.$$.fragment, _), me(c), r = !0);
    },
    o(_) {
      he(e.$$.fragment, _), he(n.$$.fragment, _), he(c), r = !1;
    },
    d(_) {
      _ && (We(t), We(i), We(s)), Ie(e, _), Ie(n, _), c.d(_);
    }
  };
}
function zs(l) {
  let e, t;
  return e = new en({
    props: {
      visible: (
        /*visible*/
        l[3]
      ),
      variant: (
        /*value*/
        l[0] === null ? "dashed" : "solid"
      ),
      border_mode: "base",
      padding: !1,
      elem_id: (
        /*elem_id*/
        l[1]
      ),
      elem_classes: (
        /*elem_classes*/
        l[2]
      ),
      container: (
        /*container*/
        l[9]
      ),
      scale: (
        /*scale*/
        l[10]
      ),
      min_width: (
        /*min_width*/
        l[11]
      ),
      allow_overflow: !1,
      height: (
        /*height*/
        l[6]
      ),
      $$slots: { default: [Ss] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      je(e.$$.fragment);
    },
    m(n, i) {
      Ne(e, n, i), t = !0;
    },
    p(n, [i]) {
      const f = {};
      i & /*visible*/
      8 && (f.visible = /*visible*/
      n[3]), i & /*value*/
      1 && (f.variant = /*value*/
      n[0] === null ? "dashed" : "solid"), i & /*elem_id*/
      2 && (f.elem_id = /*elem_id*/
      n[1]), i & /*elem_classes*/
      4 && (f.elem_classes = /*elem_classes*/
      n[2]), i & /*container*/
      512 && (f.container = /*container*/
      n[9]), i & /*scale*/
      1024 && (f.scale = /*scale*/
      n[10]), i & /*min_width*/
      2048 && (f.min_width = /*min_width*/
      n[11]), i & /*height*/
      64 && (f.height = /*height*/
      n[6]), i & /*$$scope, rerender_key, file_count, interactive, value, show_label, label, loading_status, gradio*/
      291249 && (f.$$scope = { dirty: i, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (me(e.$$.fragment, n), t = !0);
    },
    o(n) {
      he(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Ie(e, n);
    }
  };
}
function Fs(l, e, t) {
  let n, { elem_id: i = "" } = e, { elem_classes: f = [] } = e, { visible: s = !0 } = e, { value: r } = e, o, { label: a } = e, { show_label: c } = e, { height: _ = void 0 } = e, { file_count: d = "multiple" } = e, { loading_status: h } = e, { container: g = !0 } = e, { scale: y = null } = e, { min_width: C = void 0 } = e, { gradio: z } = e, { interactive: m } = e;
  const u = () => z.dispatch("clear_status", h);
  function k(b) {
    r = b, t(0, r);
  }
  return l.$$set = (b) => {
    "elem_id" in b && t(1, i = b.elem_id), "elem_classes" in b && t(2, f = b.elem_classes), "visible" in b && t(3, s = b.visible), "value" in b && t(0, r = b.value), "label" in b && t(4, a = b.label), "show_label" in b && t(5, c = b.show_label), "height" in b && t(6, _ = b.height), "file_count" in b && t(7, d = b.file_count), "loading_status" in b && t(8, h = b.loading_status), "container" in b && t(9, g = b.container), "scale" in b && t(10, y = b.scale), "min_width" in b && t(11, C = b.min_width), "gradio" in b && t(12, z = b.gradio), "interactive" in b && t(13, m = b.interactive);
  }, l.$$.update = () => {
    l.$$.dirty & /*value, old_value, gradio*/
    36865 && JSON.stringify(r) !== JSON.stringify(o) && (t(15, o = r), z.dispatch("change"));
  }, t(14, n = []), [
    r,
    i,
    f,
    s,
    a,
    c,
    _,
    d,
    h,
    g,
    y,
    C,
    z,
    m,
    n,
    o,
    u,
    k
  ];
}
class Ls extends ds {
  constructor(e) {
    super(), Cs(this, e, Fs, zs, gl, {
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      value: 0,
      label: 4,
      show_label: 5,
      height: 6,
      file_count: 7,
      loading_status: 8,
      container: 9,
      scale: 10,
      min_width: 11,
      gradio: 12,
      interactive: 13
    });
  }
  get elem_id() {
    return this.$$.ctx[1];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), E();
  }
  get elem_classes() {
    return this.$$.ctx[2];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), E();
  }
  get visible() {
    return this.$$.ctx[3];
  }
  set visible(e) {
    this.$$set({ visible: e }), E();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), E();
  }
  get label() {
    return this.$$.ctx[4];
  }
  set label(e) {
    this.$$set({ label: e }), E();
  }
  get show_label() {
    return this.$$.ctx[5];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), E();
  }
  get height() {
    return this.$$.ctx[6];
  }
  set height(e) {
    this.$$set({ height: e }), E();
  }
  get file_count() {
    return this.$$.ctx[7];
  }
  set file_count(e) {
    this.$$set({ file_count: e }), E();
  }
  get loading_status() {
    return this.$$.ctx[8];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), E();
  }
  get container() {
    return this.$$.ctx[9];
  }
  set container(e) {
    this.$$set({ container: e }), E();
  }
  get scale() {
    return this.$$.ctx[10];
  }
  set scale(e) {
    this.$$set({ scale: e }), E();
  }
  get min_width() {
    return this.$$.ctx[11];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), E();
  }
  get gradio() {
    return this.$$.ctx[12];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), E();
  }
  get interactive() {
    return this.$$.ctx[13];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), E();
  }
}
export {
  Ls as default
};
