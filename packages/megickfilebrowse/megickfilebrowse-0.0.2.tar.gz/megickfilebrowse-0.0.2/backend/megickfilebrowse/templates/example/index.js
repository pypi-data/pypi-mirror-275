const {
  SvelteComponent: z,
  append: h,
  attr: w,
  destroy_each: C,
  detach: o,
  element: d,
  empty: N,
  ensure_array_like: y,
  init: q,
  insert: u,
  noop: g,
  safe_not_equal: E,
  set_data: S,
  space: j,
  text: b,
  toggle_class: _
} = window.__gradio__svelte__internal;
function k(s, e, l) {
  const i = s.slice();
  return i[3] = e[l], i;
}
function v(s) {
  let e, l = Array.isArray(
    /*value*/
    s[0]
  ) && /*value*/
  s[0].length > 3, i, a = y(Array.isArray(
    /*value*/
    s[0]
  ) ? (
    /*value*/
    s[0].slice(0, 3)
  ) : [
    /*value*/
    s[0]
  ]), f = [];
  for (let t = 0; t < a.length; t += 1)
    f[t] = A(k(s, a, t));
  let n = l && p();
  return {
    c() {
      for (let t = 0; t < f.length; t += 1)
        f[t].c();
      e = j(), n && n.c(), i = N();
    },
    m(t, c) {
      for (let r = 0; r < f.length; r += 1)
        f[r] && f[r].m(t, c);
      u(t, e, c), n && n.m(t, c), u(t, i, c);
    },
    p(t, c) {
      if (c & /*Array, value*/
      1) {
        a = y(Array.isArray(
          /*value*/
          t[0]
        ) ? (
          /*value*/
          t[0].slice(0, 3)
        ) : [
          /*value*/
          t[0]
        ]);
        let r;
        for (r = 0; r < a.length; r += 1) {
          const m = k(t, a, r);
          f[r] ? f[r].p(m, c) : (f[r] = A(m), f[r].c(), f[r].m(e.parentNode, e));
        }
        for (; r < f.length; r += 1)
          f[r].d(1);
        f.length = a.length;
      }
      c & /*value*/
      1 && (l = Array.isArray(
        /*value*/
        t[0]
      ) && /*value*/
      t[0].length > 3), l ? n || (n = p(), n.c(), n.m(i.parentNode, i)) : n && (n.d(1), n = null);
    },
    d(t) {
      t && (o(e), o(i)), C(f, t), n && n.d(t);
    }
  };
}
function A(s) {
  let e, l, i, a = (
    /*path*/
    s[3] + ""
  ), f;
  return {
    c() {
      e = d("li"), l = d("code"), i = b("./"), f = b(a);
    },
    m(n, t) {
      u(n, e, t), h(e, l), h(l, i), h(l, f);
    },
    p(n, t) {
      t & /*value*/
      1 && a !== (a = /*path*/
      n[3] + "") && S(f, a);
    },
    d(n) {
      n && o(e);
    }
  };
}
function p(s) {
  let e;
  return {
    c() {
      e = d("li"), e.textContent = "...", w(e, "class", "extra svelte-1u88z5n");
    },
    m(l, i) {
      u(l, e, i);
    },
    d(l) {
      l && o(e);
    }
  };
}
function B(s) {
  let e, l = (
    /*value*/
    s[0] && v(s)
  );
  return {
    c() {
      e = d("ul"), l && l.c(), w(e, "class", "svelte-1u88z5n"), _(
        e,
        "table",
        /*type*/
        s[1] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        s[1] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        s[2]
      );
    },
    m(i, a) {
      u(i, e, a), l && l.m(e, null);
    },
    p(i, [a]) {
      /*value*/
      i[0] ? l ? l.p(i, a) : (l = v(i), l.c(), l.m(e, null)) : l && (l.d(1), l = null), a & /*type*/
      2 && _(
        e,
        "table",
        /*type*/
        i[1] === "table"
      ), a & /*type*/
      2 && _(
        e,
        "gallery",
        /*type*/
        i[1] === "gallery"
      ), a & /*selected*/
      4 && _(
        e,
        "selected",
        /*selected*/
        i[2]
      );
    },
    i: g,
    o: g,
    d(i) {
      i && o(e), l && l.d();
    }
  };
}
function D(s, e, l) {
  let { value: i } = e, { type: a } = e, { selected: f = !1 } = e;
  return s.$$set = (n) => {
    "value" in n && l(0, i = n.value), "type" in n && l(1, a = n.type), "selected" in n && l(2, f = n.selected);
  }, [i, a, f];
}
class F extends z {
  constructor(e) {
    super(), q(this, e, D, B, E, { value: 0, type: 1, selected: 2 });
  }
}
export {
  F as default
};
