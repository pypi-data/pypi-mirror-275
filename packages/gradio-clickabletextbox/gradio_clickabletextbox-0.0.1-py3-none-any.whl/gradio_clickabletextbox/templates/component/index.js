const {
  SvelteComponent: wl,
  assign: vl,
  create_slot: kl,
  detach: pl,
  element: Cl,
  get_all_dirty_from_scope: yl,
  get_slot_changes: Ll,
  get_spread_update: Ml,
  init: Vl,
  insert: ql,
  safe_not_equal: Hl,
  set_dynamic_element_data: ct,
  set_style: K,
  toggle_class: se,
  transition_in: ll,
  transition_out: nl,
  update_slot_base: Zl
} = window.__gradio__svelte__internal;
function Fl(l) {
  let e, t, n;
  const s = (
    /*#slots*/
    l[18].default
  ), i = kl(
    s,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let f = [
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
  ], a = {};
  for (let r = 0; r < f.length; r += 1)
    a = vl(a, f[r]);
  return {
    c() {
      e = Cl(
        /*tag*/
        l[14]
      ), i && i.c(), ct(
        /*tag*/
        l[14]
      )(e, a), se(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), se(
        e,
        "padded",
        /*padding*/
        l[6]
      ), se(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), se(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), se(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), K(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), K(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), K(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), K(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), K(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), K(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), K(e, "border-width", "var(--block-border-width)");
    },
    m(r, o) {
      ql(r, e, o), i && i.m(e, null), n = !0;
    },
    p(r, o) {
      i && i.p && (!n || o & /*$$scope*/
      131072) && Zl(
        i,
        s,
        r,
        /*$$scope*/
        r[17],
        n ? Ll(
          s,
          /*$$scope*/
          r[17],
          o,
          null
        ) : yl(
          /*$$scope*/
          r[17]
        ),
        null
      ), ct(
        /*tag*/
        r[14]
      )(e, a = Ml(f, [
        (!n || o & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!n || o & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!n || o & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), se(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), se(
        e,
        "padded",
        /*padding*/
        r[6]
      ), se(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), se(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), se(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), o & /*height*/
      1 && K(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), o & /*width*/
      2 && K(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), o & /*variant*/
      16 && K(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), o & /*allow_overflow*/
      2048 && K(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), o & /*scale*/
      4096 && K(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), o & /*min_width*/
      8192 && K(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      n || (ll(i, r), n = !0);
    },
    o(r) {
      nl(i, r), n = !1;
    },
    d(r) {
      r && pl(e), i && i.d(r);
    }
  };
}
function Sl(l) {
  let e, t = (
    /*tag*/
    l[14] && Fl(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, s) {
      t && t.m(n, s), e = !0;
    },
    p(n, [s]) {
      /*tag*/
      n[14] && t.p(n, s);
    },
    i(n) {
      e || (ll(t, n), e = !0);
    },
    o(n) {
      nl(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function zl(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { height: i = void 0 } = e, { width: f = void 0 } = e, { elem_id: a = "" } = e, { elem_classes: r = [] } = e, { variant: o = "solid" } = e, { border_mode: u = "base" } = e, { padding: _ = !0 } = e, { type: d = "normal" } = e, { test_id: h = void 0 } = e, { explicit_call: M = !1 } = e, { container: H = !0 } = e, { visible: k = !0 } = e, { allow_overflow: Z = !0 } = e, { scale: c = null } = e, { min_width: m = 0 } = e, p = d === "fieldset" ? "fieldset" : "div";
  const V = (w) => {
    if (w !== void 0) {
      if (typeof w == "number")
        return w + "px";
      if (typeof w == "string")
        return w;
    }
  };
  return l.$$set = (w) => {
    "height" in w && t(0, i = w.height), "width" in w && t(1, f = w.width), "elem_id" in w && t(2, a = w.elem_id), "elem_classes" in w && t(3, r = w.elem_classes), "variant" in w && t(4, o = w.variant), "border_mode" in w && t(5, u = w.border_mode), "padding" in w && t(6, _ = w.padding), "type" in w && t(16, d = w.type), "test_id" in w && t(7, h = w.test_id), "explicit_call" in w && t(8, M = w.explicit_call), "container" in w && t(9, H = w.container), "visible" in w && t(10, k = w.visible), "allow_overflow" in w && t(11, Z = w.allow_overflow), "scale" in w && t(12, c = w.scale), "min_width" in w && t(13, m = w.min_width), "$$scope" in w && t(17, s = w.$$scope);
  }, [
    i,
    f,
    a,
    r,
    o,
    u,
    _,
    h,
    M,
    H,
    k,
    Z,
    c,
    m,
    p,
    V,
    d,
    s,
    n
  ];
}
class El extends wl {
  constructor(e) {
    super(), Vl(this, e, zl, Sl, Hl, {
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
  SvelteComponent: Tl,
  attr: Bl,
  create_slot: Nl,
  detach: Dl,
  element: Il,
  get_all_dirty_from_scope: jl,
  get_slot_changes: Al,
  init: Pl,
  insert: Yl,
  safe_not_equal: Kl,
  transition_in: Ul,
  transition_out: Xl,
  update_slot_base: Gl
} = window.__gradio__svelte__internal;
function Ol(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[1].default
  ), s = Nl(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      e = Il("div"), s && s.c(), Bl(e, "class", "svelte-1hnfib2");
    },
    m(i, f) {
      Yl(i, e, f), s && s.m(e, null), t = !0;
    },
    p(i, [f]) {
      s && s.p && (!t || f & /*$$scope*/
      1) && Gl(
        s,
        n,
        i,
        /*$$scope*/
        i[0],
        t ? Al(
          n,
          /*$$scope*/
          i[0],
          f,
          null
        ) : jl(
          /*$$scope*/
          i[0]
        ),
        null
      );
    },
    i(i) {
      t || (Ul(s, i), t = !0);
    },
    o(i) {
      Xl(s, i), t = !1;
    },
    d(i) {
      i && Dl(e), s && s.d(i);
    }
  };
}
function Rl(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e;
  return l.$$set = (i) => {
    "$$scope" in i && t(0, s = i.$$scope);
  }, [s, n];
}
class Wl extends Tl {
  constructor(e) {
    super(), Pl(this, e, Rl, Ol, Kl, {});
  }
}
const {
  SvelteComponent: Jl,
  attr: dt,
  check_outros: Ql,
  create_component: xl,
  create_slot: $l,
  destroy_component: en,
  detach: De,
  element: tn,
  empty: ln,
  get_all_dirty_from_scope: nn,
  get_slot_changes: sn,
  group_outros: fn,
  init: on,
  insert: Ie,
  mount_component: an,
  safe_not_equal: rn,
  set_data: un,
  space: _n,
  text: cn,
  toggle_class: ye,
  transition_in: ze,
  transition_out: je,
  update_slot_base: dn
} = window.__gradio__svelte__internal;
function mt(l) {
  let e, t;
  return e = new Wl({
    props: {
      $$slots: { default: [mn] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      xl(e.$$.fragment);
    },
    m(n, s) {
      an(e, n, s), t = !0;
    },
    p(n, s) {
      const i = {};
      s & /*$$scope, info*/
      10 && (i.$$scope = { dirty: s, ctx: n }), e.$set(i);
    },
    i(n) {
      t || (ze(e.$$.fragment, n), t = !0);
    },
    o(n) {
      je(e.$$.fragment, n), t = !1;
    },
    d(n) {
      en(e, n);
    }
  };
}
function mn(l) {
  let e;
  return {
    c() {
      e = cn(
        /*info*/
        l[1]
      );
    },
    m(t, n) {
      Ie(t, e, n);
    },
    p(t, n) {
      n & /*info*/
      2 && un(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && De(e);
    }
  };
}
function hn(l) {
  let e, t, n, s;
  const i = (
    /*#slots*/
    l[2].default
  ), f = $l(
    i,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let a = (
    /*info*/
    l[1] && mt(l)
  );
  return {
    c() {
      e = tn("span"), f && f.c(), t = _n(), a && a.c(), n = ln(), dt(e, "data-testid", "block-info"), dt(e, "class", "svelte-22c38v"), ye(e, "sr-only", !/*show_label*/
      l[0]), ye(e, "hide", !/*show_label*/
      l[0]), ye(
        e,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(r, o) {
      Ie(r, e, o), f && f.m(e, null), Ie(r, t, o), a && a.m(r, o), Ie(r, n, o), s = !0;
    },
    p(r, [o]) {
      f && f.p && (!s || o & /*$$scope*/
      8) && dn(
        f,
        i,
        r,
        /*$$scope*/
        r[3],
        s ? sn(
          i,
          /*$$scope*/
          r[3],
          o,
          null
        ) : nn(
          /*$$scope*/
          r[3]
        ),
        null
      ), (!s || o & /*show_label*/
      1) && ye(e, "sr-only", !/*show_label*/
      r[0]), (!s || o & /*show_label*/
      1) && ye(e, "hide", !/*show_label*/
      r[0]), (!s || o & /*info*/
      2) && ye(
        e,
        "has-info",
        /*info*/
        r[1] != null
      ), /*info*/
      r[1] ? a ? (a.p(r, o), o & /*info*/
      2 && ze(a, 1)) : (a = mt(r), a.c(), ze(a, 1), a.m(n.parentNode, n)) : a && (fn(), je(a, 1, 1, () => {
        a = null;
      }), Ql());
    },
    i(r) {
      s || (ze(f, r), ze(a), s = !0);
    },
    o(r) {
      je(f, r), je(a), s = !1;
    },
    d(r) {
      r && (De(e), De(t), De(n)), f && f.d(r), a && a.d(r);
    }
  };
}
function bn(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { show_label: i = !0 } = e, { info: f = void 0 } = e;
  return l.$$set = (a) => {
    "show_label" in a && t(0, i = a.show_label), "info" in a && t(1, f = a.info), "$$scope" in a && t(3, s = a.$$scope);
  }, [i, f, n, s];
}
class gn extends Jl {
  constructor(e) {
    super(), on(this, e, bn, hn, rn, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: wn,
  append: tt,
  attr: me,
  bubble: vn,
  create_component: kn,
  destroy_component: pn,
  detach: il,
  element: lt,
  init: Cn,
  insert: sl,
  listen: yn,
  mount_component: Ln,
  safe_not_equal: Mn,
  set_data: Vn,
  set_style: Le,
  space: qn,
  text: Hn,
  toggle_class: A,
  transition_in: Zn,
  transition_out: Fn
} = window.__gradio__svelte__internal;
function ht(l) {
  let e, t;
  return {
    c() {
      e = lt("span"), t = Hn(
        /*label*/
        l[1]
      ), me(e, "class", "svelte-1lrphxw");
    },
    m(n, s) {
      sl(n, e, s), tt(e, t);
    },
    p(n, s) {
      s & /*label*/
      2 && Vn(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && il(e);
    }
  };
}
function Sn(l) {
  let e, t, n, s, i, f, a, r = (
    /*show_label*/
    l[2] && ht(l)
  );
  return s = new /*Icon*/
  l[0]({}), {
    c() {
      e = lt("button"), r && r.c(), t = qn(), n = lt("div"), kn(s.$$.fragment), me(n, "class", "svelte-1lrphxw"), A(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), A(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), A(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], me(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), me(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), me(
        e,
        "title",
        /*label*/
        l[1]
      ), me(e, "class", "svelte-1lrphxw"), A(
        e,
        "pending",
        /*pending*/
        l[3]
      ), A(
        e,
        "padded",
        /*padded*/
        l[5]
      ), A(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), A(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), Le(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), Le(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), Le(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(o, u) {
      sl(o, e, u), r && r.m(e, null), tt(e, t), tt(e, n), Ln(s, n, null), i = !0, f || (a = yn(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), f = !0);
    },
    p(o, [u]) {
      /*show_label*/
      o[2] ? r ? r.p(o, u) : (r = ht(o), r.c(), r.m(e, t)) : r && (r.d(1), r = null), (!i || u & /*size*/
      16) && A(
        n,
        "small",
        /*size*/
        o[4] === "small"
      ), (!i || u & /*size*/
      16) && A(
        n,
        "large",
        /*size*/
        o[4] === "large"
      ), (!i || u & /*size*/
      16) && A(
        n,
        "medium",
        /*size*/
        o[4] === "medium"
      ), (!i || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      o[7]), (!i || u & /*label*/
      2) && me(
        e,
        "aria-label",
        /*label*/
        o[1]
      ), (!i || u & /*hasPopup*/
      256) && me(
        e,
        "aria-haspopup",
        /*hasPopup*/
        o[8]
      ), (!i || u & /*label*/
      2) && me(
        e,
        "title",
        /*label*/
        o[1]
      ), (!i || u & /*pending*/
      8) && A(
        e,
        "pending",
        /*pending*/
        o[3]
      ), (!i || u & /*padded*/
      32) && A(
        e,
        "padded",
        /*padded*/
        o[5]
      ), (!i || u & /*highlight*/
      64) && A(
        e,
        "highlight",
        /*highlight*/
        o[6]
      ), (!i || u & /*transparent*/
      512) && A(
        e,
        "transparent",
        /*transparent*/
        o[9]
      ), u & /*disabled, _color*/
      4224 && Le(e, "color", !/*disabled*/
      o[7] && /*_color*/
      o[12] ? (
        /*_color*/
        o[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && Le(e, "--bg-color", /*disabled*/
      o[7] ? "auto" : (
        /*background*/
        o[10]
      )), u & /*offset*/
      2048 && Le(
        e,
        "margin-left",
        /*offset*/
        o[11] + "px"
      );
    },
    i(o) {
      i || (Zn(s.$$.fragment, o), i = !0);
    },
    o(o) {
      Fn(s.$$.fragment, o), i = !1;
    },
    d(o) {
      o && il(e), r && r.d(), pn(s), f = !1, a();
    }
  };
}
function zn(l, e, t) {
  let n, { Icon: s } = e, { label: i = "" } = e, { show_label: f = !1 } = e, { pending: a = !1 } = e, { size: r = "small" } = e, { padded: o = !0 } = e, { highlight: u = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: d = !1 } = e, { color: h = "var(--block-label-text-color)" } = e, { transparent: M = !1 } = e, { background: H = "var(--background-fill-primary)" } = e, { offset: k = 0 } = e;
  function Z(c) {
    vn.call(this, l, c);
  }
  return l.$$set = (c) => {
    "Icon" in c && t(0, s = c.Icon), "label" in c && t(1, i = c.label), "show_label" in c && t(2, f = c.show_label), "pending" in c && t(3, a = c.pending), "size" in c && t(4, r = c.size), "padded" in c && t(5, o = c.padded), "highlight" in c && t(6, u = c.highlight), "disabled" in c && t(7, _ = c.disabled), "hasPopup" in c && t(8, d = c.hasPopup), "color" in c && t(13, h = c.color), "transparent" in c && t(9, M = c.transparent), "background" in c && t(10, H = c.background), "offset" in c && t(11, k = c.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = u ? "var(--color-accent)" : h);
  }, [
    s,
    i,
    f,
    a,
    r,
    o,
    u,
    _,
    d,
    M,
    H,
    k,
    n,
    h,
    Z
  ];
}
class En extends wn {
  constructor(e) {
    super(), Cn(this, e, zn, Sn, Mn, {
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
const {
  SvelteComponent: Tn,
  append: We,
  attr: Q,
  detach: Bn,
  init: Nn,
  insert: Dn,
  noop: Je,
  safe_not_equal: In,
  set_style: fe,
  svg_element: Te
} = window.__gradio__svelte__internal;
function jn(l) {
  let e, t, n, s;
  return {
    c() {
      e = Te("svg"), t = Te("g"), n = Te("path"), s = Te("path"), Q(n, "d", "M18,6L6.087,17.913"), fe(n, "fill", "none"), fe(n, "fill-rule", "nonzero"), fe(n, "stroke-width", "2px"), Q(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), Q(s, "d", "M4.364,4.364L19.636,19.636"), fe(s, "fill", "none"), fe(s, "fill-rule", "nonzero"), fe(s, "stroke-width", "2px"), Q(e, "width", "100%"), Q(e, "height", "100%"), Q(e, "viewBox", "0 0 24 24"), Q(e, "version", "1.1"), Q(e, "xmlns", "http://www.w3.org/2000/svg"), Q(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), Q(e, "xml:space", "preserve"), Q(e, "stroke", "currentColor"), fe(e, "fill-rule", "evenodd"), fe(e, "clip-rule", "evenodd"), fe(e, "stroke-linecap", "round"), fe(e, "stroke-linejoin", "round");
    },
    m(i, f) {
      Dn(i, e, f), We(e, t), We(t, n), We(e, s);
    },
    p: Je,
    i: Je,
    o: Je,
    d(i) {
      i && Bn(e);
    }
  };
}
class An extends Tn {
  constructor(e) {
    super(), Nn(this, e, null, jn, In, {});
  }
}
const Pn = [
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
], bt = {
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
Pn.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: bt[e][t],
      secondary: bt[e][n]
    }
  }),
  {}
);
function Ae() {
}
const Yn = (l) => l;
function Kn(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const fl = typeof window < "u";
let gt = fl ? () => window.performance.now() : () => Date.now(), ol = fl ? (l) => requestAnimationFrame(l) : Ae;
const Ze = /* @__PURE__ */ new Set();
function al(l) {
  Ze.forEach((e) => {
    e.c(l) || (Ze.delete(e), e.f());
  }), Ze.size !== 0 && ol(al);
}
function Un(l) {
  let e;
  return Ze.size === 0 && ol(al), {
    promise: new Promise((t) => {
      Ze.add(e = { c: l, f: t });
    }),
    abort() {
      Ze.delete(e);
    }
  };
}
function wt(l, { delay: e = 0, duration: t = 400, easing: n = Yn } = {}) {
  const s = +getComputedStyle(l).opacity;
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (i) => `opacity: ${i * s}`
  };
}
const Me = [];
function Xn(l, e = Ae) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function s(a) {
    if (Kn(l, a) && (l = a, t)) {
      const r = !Me.length;
      for (const o of n)
        o[1](), Me.push(o, l);
      if (r) {
        for (let o = 0; o < Me.length; o += 2)
          Me[o][0](Me[o + 1]);
        Me.length = 0;
      }
    }
  }
  function i(a) {
    s(a(l));
  }
  function f(a, r = Ae) {
    const o = [a, r];
    return n.add(o), n.size === 1 && (t = e(s, i) || Ae), a(l), () => {
      n.delete(o), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: s, update: i, subscribe: f };
}
function vt(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function nt(l, e, t, n) {
  if (typeof t == "number" || vt(t)) {
    const s = n - t, i = (t - e) / (l.dt || 1 / 60), f = l.opts.stiffness * s, a = l.opts.damping * i, r = (f - a) * l.inv_mass, o = (i + r) * l.dt;
    return Math.abs(o) < l.opts.precision && Math.abs(s) < l.opts.precision ? n : (l.settled = !1, vt(t) ? new Date(t.getTime() + o) : t + o);
  } else {
    if (Array.isArray(t))
      return t.map(
        (s, i) => nt(l, e[i], t[i], n[i])
      );
    if (typeof t == "object") {
      const s = {};
      for (const i in t)
        s[i] = nt(l, e[i], t[i], n[i]);
      return s;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function kt(l, e = {}) {
  const t = Xn(l), { stiffness: n = 0.15, damping: s = 0.8, precision: i = 0.01 } = e;
  let f, a, r, o = l, u = l, _ = 1, d = 0, h = !1;
  function M(k, Z = {}) {
    u = k;
    const c = r = {};
    return l == null || Z.hard || H.stiffness >= 1 && H.damping >= 1 ? (h = !0, f = gt(), o = k, t.set(l = u), Promise.resolve()) : (Z.soft && (d = 1 / ((Z.soft === !0 ? 0.5 : +Z.soft) * 60), _ = 0), a || (f = gt(), h = !1, a = Un((m) => {
      if (h)
        return h = !1, a = null, !1;
      _ = Math.min(_ + d, 1);
      const p = {
        inv_mass: _,
        opts: H,
        settled: !0,
        dt: (m - f) * 60 / 1e3
      }, V = nt(p, o, l, u);
      return f = m, o = l, t.set(l = V), p.settled && (a = null), !p.settled;
    })), new Promise((m) => {
      a.promise.then(() => {
        c === r && m();
      });
    }));
  }
  const H = {
    set: M,
    update: (k, Z) => M(k(u, l), Z),
    subscribe: t.subscribe,
    stiffness: n,
    damping: s,
    precision: i
  };
  return H;
}
const {
  SvelteComponent: Gn,
  action_destroyer: On,
  add_render_callback: Rn,
  append: S,
  attr: C,
  binding_callbacks: Wn,
  bubble: pt,
  check_outros: Jn,
  create_bidirectional_transition: Ct,
  create_component: Qn,
  destroy_component: xn,
  destroy_each: rl,
  detach: ue,
  element: I,
  ensure_array_like: Pe,
  group_outros: $n,
  init: ei,
  insert: _e,
  is_function: ti,
  listen: oe,
  mount_component: li,
  noop: Qe,
  run_all: ni,
  safe_not_equal: ii,
  set_data: ot,
  set_input_value: yt,
  space: ce,
  svg_element: Ye,
  text: at,
  toggle_class: Lt,
  transition_in: xe,
  transition_out: $e
} = window.__gradio__svelte__internal, { beforeUpdate: si, afterUpdate: fi, createEventDispatcher: oi, tick: Mt } = window.__gradio__svelte__internal;
function Vt(l, e, t) {
  const n = l.slice();
  return n[39] = e[t], n;
}
function qt(l, e, t) {
  const n = l.slice();
  return n[39] = e[t], n;
}
function ai(l) {
  let e;
  return {
    c() {
      e = at(
        /*label*/
        l[3]
      );
    },
    m(t, n) {
      _e(t, e, n);
    },
    p(t, n) {
      n[0] & /*label*/
      8 && ot(
        e,
        /*label*/
        t[3]
      );
    },
    d(t) {
      t && ue(e);
    }
  };
}
function ri(l) {
  let e, t, n;
  return {
    c() {
      e = I("button"), e.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-n6pmag"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#CCCCCC" class="svelte-n6pmag"></path></svg>', C(e, "class", "extend_button svelte-n6pmag"), C(e, "aria-label", "Extend"), C(e, "aria-roledescription", "Extend text");
    },
    m(s, i) {
      _e(s, e, i), t || (n = oe(
        e,
        "click",
        /*handle_extension*/
        l[15]
      ), t = !0);
    },
    p: Qe,
    i: Qe,
    o: Qe,
    d(s) {
      s && ue(e), t = !1, n();
    }
  };
}
function ui(l) {
  let e, t, n, s, i, f, a, r, o = (
    /*prompts*/
    l[8].length > 0 && Ht(l)
  ), u = (
    /*suffixes*/
    l[9].length > 0 && Ft(l)
  );
  return {
    c() {
      e = I("button"), e.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-n6pmag"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#ff6700" class="svelte-n6pmag"></path></svg>', t = ce(), n = I("div"), o && o.c(), s = ce(), u && u.c(), C(e, "class", "extend_button svelte-n6pmag"), C(e, "aria-label", "Extend"), C(e, "aria-roledescription", "Extend text"), C(n, "class", "menu svelte-n6pmag");
    },
    m(_, d) {
      _e(_, e, d), _e(_, t, d), _e(_, n, d), o && o.m(n, null), S(n, s), u && u.m(n, null), f = !0, a || (r = oe(
        e,
        "click",
        /*handle_extension*/
        l[15]
      ), a = !0);
    },
    p(_, d) {
      /*prompts*/
      _[8].length > 0 ? o ? o.p(_, d) : (o = Ht(_), o.c(), o.m(n, s)) : o && (o.d(1), o = null), /*suffixes*/
      _[9].length > 0 ? u ? u.p(_, d) : (u = Ft(_), u.c(), u.m(n, null)) : u && (u.d(1), u = null);
    },
    i(_) {
      f || (_ && Rn(() => {
        f && (i || (i = Ct(n, wt, {}, !0)), i.run(1));
      }), f = !0);
    },
    o(_) {
      _ && (i || (i = Ct(n, wt, {}, !1)), i.run(0)), f = !1;
    },
    d(_) {
      _ && (ue(e), ue(t), ue(n)), o && o.d(), u && u.d(), _ && i && i.end(), a = !1, r();
    }
  };
}
function Ht(l) {
  let e, t, n, s, i = Pe(
    /*prompts*/
    l[8]
  ), f = [];
  for (let a = 0; a < i.length; a += 1)
    f[a] = Zt(qt(l, i, a));
  return {
    c() {
      e = I("div"), t = I("span"), t.textContent = "Best prompt structures", n = ce(), s = I("ul");
      for (let a = 0; a < f.length; a += 1)
        f[a].c();
      C(s, "class", "svelte-n6pmag"), C(e, "class", "menu_section svelte-n6pmag");
    },
    m(a, r) {
      _e(a, e, r), S(e, t), S(e, n), S(e, s);
      for (let o = 0; o < f.length; o += 1)
        f[o] && f[o].m(s, null);
    },
    p(a, r) {
      if (r[0] & /*addToTextbox, prompts*/
      65792) {
        i = Pe(
          /*prompts*/
          a[8]
        );
        let o;
        for (o = 0; o < i.length; o += 1) {
          const u = qt(a, i, o);
          f[o] ? f[o].p(u, r) : (f[o] = Zt(u), f[o].c(), f[o].m(s, null));
        }
        for (; o < f.length; o += 1)
          f[o].d(1);
        f.length = i.length;
      }
    },
    d(a) {
      a && ue(e), rl(f, a);
    }
  };
}
function Zt(l) {
  let e, t, n = (
    /*word*/
    l[39] + ""
  ), s, i, f, a, r, o, u;
  function _() {
    return (
      /*click_handler*/
      l[29](
        /*word*/
        l[39]
      )
    );
  }
  return {
    c() {
      e = I("li"), t = I("button"), s = at(n), i = ce(), f = Ye("svg"), a = Ye("path"), r = ce(), C(a, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), C(a, "fill", "#FF9A57"), C(a, "class", "svelte-n6pmag"), C(f, "xmlns", "http://www.w3.org/2000/svg"), C(f, "width", "11"), C(f, "height", "12"), C(f, "viewBox", "0 0 11 12"), C(f, "fill", "none"), C(f, "class", "svelte-n6pmag"), C(t, "class", "text_extension_button_prompt svelte-n6pmag"), C(e, "class", "svelte-n6pmag");
    },
    m(d, h) {
      _e(d, e, h), S(e, t), S(t, s), S(t, i), S(t, f), S(f, a), S(e, r), o || (u = oe(t, "click", _), o = !0);
    },
    p(d, h) {
      l = d, h[0] & /*prompts*/
      256 && n !== (n = /*word*/
      l[39] + "") && ot(s, n);
    },
    d(d) {
      d && ue(e), o = !1, u();
    }
  };
}
function Ft(l) {
  let e, t, n, s, i = Pe(
    /*suffixes*/
    l[9]
  ), f = [];
  for (let a = 0; a < i.length; a += 1)
    f[a] = St(Vt(l, i, a));
  return {
    c() {
      e = I("div"), t = I("span"), t.textContent = "Best style keywords", n = ce(), s = I("ul");
      for (let a = 0; a < f.length; a += 1)
        f[a].c();
      C(s, "class", "svelte-n6pmag"), C(e, "class", "menu_section svelte-n6pmag");
    },
    m(a, r) {
      _e(a, e, r), S(e, t), S(e, n), S(e, s);
      for (let o = 0; o < f.length; o += 1)
        f[o] && f[o].m(s, null);
    },
    p(a, r) {
      if (r[0] & /*addToTextbox, suffixes*/
      66048) {
        i = Pe(
          /*suffixes*/
          a[9]
        );
        let o;
        for (o = 0; o < i.length; o += 1) {
          const u = Vt(a, i, o);
          f[o] ? f[o].p(u, r) : (f[o] = St(u), f[o].c(), f[o].m(s, null));
        }
        for (; o < f.length; o += 1)
          f[o].d(1);
        f.length = i.length;
      }
    },
    d(a) {
      a && ue(e), rl(f, a);
    }
  };
}
function St(l) {
  let e, t, n = (
    /*word*/
    l[39] + ""
  ), s, i, f, a, r, o, u;
  function _() {
    return (
      /*click_handler_1*/
      l[30](
        /*word*/
        l[39]
      )
    );
  }
  return {
    c() {
      e = I("li"), t = I("button"), s = at(n), i = ce(), f = Ye("svg"), a = Ye("path"), r = ce(), C(a, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), C(a, "fill", "#FF9A57"), C(a, "class", "svelte-n6pmag"), C(f, "xmlns", "http://www.w3.org/2000/svg"), C(f, "width", "11"), C(f, "height", "12"), C(f, "viewBox", "0 0 11 12"), C(f, "fill", "none"), C(f, "class", "svelte-n6pmag"), C(t, "class", "text_extension_button svelte-n6pmag"), C(e, "class", "svelte-n6pmag");
    },
    m(d, h) {
      _e(d, e, h), S(e, t), S(t, s), S(t, i), S(t, f), S(f, a), S(e, r), o || (u = oe(t, "click", _), o = !0);
    },
    p(d, h) {
      l = d, h[0] & /*suffixes*/
      512 && n !== (n = /*word*/
      l[39] + "") && ot(s, n);
    },
    d(d) {
      d && ue(e), o = !1, u();
    }
  };
}
function _i(l) {
  let e, t, n, s, i, f, a, r, o, u, _, d, h, M;
  t = new gn({
    props: {
      show_label: (
        /*show_label*/
        l[6]
      ),
      info: (
        /*info*/
        l[4]
      ),
      $$slots: { default: [ai] },
      $$scope: { ctx: l }
    }
  });
  const H = [ui, ri], k = [];
  function Z(c, m) {
    return (
      /*show_menu*/
      c[14] && /*prompts*/
      (c[8].length > 0 || /*suffixes*/
      c[9].length > 0) ? 0 : (
        /*prompts*/
        c[8].length > 0 || /*suffixes*/
        c[9].length > 0 ? 1 : -1
      )
    );
  }
  return ~(u = Z(l)) && (_ = k[u] = H[u](l)), {
    c() {
      e = I("label"), Qn(t.$$.fragment), n = ce(), s = I("div"), i = I("textarea"), o = ce(), _ && _.c(), C(i, "data-testid", "textbox"), C(i, "class", "scroll-hide svelte-n6pmag"), C(i, "dir", f = /*rtl*/
      l[10] ? "rtl" : "ltr"), C(
        i,
        "placeholder",
        /*placeholder*/
        l[2]
      ), C(
        i,
        "rows",
        /*lines*/
        l[1]
      ), i.disabled = /*disabled*/
      l[5], i.autofocus = /*autofocus*/
      l[11], C(i, "style", a = /*text_align*/
      l[12] ? "text-align: " + /*text_align*/
      l[12] : ""), C(s, "class", "input-container"), C(e, "class", "svelte-n6pmag"), Lt(
        e,
        "container",
        /*container*/
        l[7]
      );
    },
    m(c, m) {
      _e(c, e, m), li(t, e, null), S(e, n), S(e, s), S(s, i), yt(
        i,
        /*value*/
        l[0]
      ), l[28](i), S(s, o), ~u && k[u].m(s, null), d = !0, /*autofocus*/
      l[11] && i.focus(), h || (M = [
        On(r = /*text_area_resize*/
        l[20].call(
          null,
          i,
          /*value*/
          l[0]
        )),
        oe(
          i,
          "input",
          /*textarea_input_handler*/
          l[27]
        ),
        oe(
          i,
          "keypress",
          /*handle_keypress*/
          l[18]
        ),
        oe(
          i,
          "blur",
          /*blur_handler*/
          l[25]
        ),
        oe(
          i,
          "select",
          /*handle_select*/
          l[17]
        ),
        oe(
          i,
          "focus",
          /*focus_handler*/
          l[26]
        ),
        oe(
          i,
          "scroll",
          /*handle_scroll*/
          l[19]
        )
      ], h = !0);
    },
    p(c, m) {
      const p = {};
      m[0] & /*show_label*/
      64 && (p.show_label = /*show_label*/
      c[6]), m[0] & /*info*/
      16 && (p.info = /*info*/
      c[4]), m[0] & /*label*/
      8 | m[1] & /*$$scope*/
      8192 && (p.$$scope = { dirty: m, ctx: c }), t.$set(p), (!d || m[0] & /*rtl*/
      1024 && f !== (f = /*rtl*/
      c[10] ? "rtl" : "ltr")) && C(i, "dir", f), (!d || m[0] & /*placeholder*/
      4) && C(
        i,
        "placeholder",
        /*placeholder*/
        c[2]
      ), (!d || m[0] & /*lines*/
      2) && C(
        i,
        "rows",
        /*lines*/
        c[1]
      ), (!d || m[0] & /*disabled*/
      32) && (i.disabled = /*disabled*/
      c[5]), (!d || m[0] & /*autofocus*/
      2048) && (i.autofocus = /*autofocus*/
      c[11]), (!d || m[0] & /*text_align*/
      4096 && a !== (a = /*text_align*/
      c[12] ? "text-align: " + /*text_align*/
      c[12] : "")) && C(i, "style", a), r && ti(r.update) && m[0] & /*value*/
      1 && r.update.call(
        null,
        /*value*/
        c[0]
      ), m[0] & /*value*/
      1 && yt(
        i,
        /*value*/
        c[0]
      );
      let V = u;
      u = Z(c), u === V ? ~u && k[u].p(c, m) : (_ && ($n(), $e(k[V], 1, 1, () => {
        k[V] = null;
      }), Jn()), ~u ? (_ = k[u], _ ? _.p(c, m) : (_ = k[u] = H[u](c), _.c()), xe(_, 1), _.m(s, null)) : _ = null), (!d || m[0] & /*container*/
      128) && Lt(
        e,
        "container",
        /*container*/
        c[7]
      );
    },
    i(c) {
      d || (xe(t.$$.fragment, c), xe(_), d = !0);
    },
    o(c) {
      $e(t.$$.fragment, c), $e(_), d = !1;
    },
    d(c) {
      c && ue(e), xn(t), l[28](null), ~u && k[u].d(), h = !1, ni(M);
    }
  };
}
function ci(l, e, t) {
  var n = this && this.__awaiter || function(b, T, B, N) {
    function Y(ie) {
      return ie instanceof B ? ie : new B(function(Ce) {
        Ce(ie);
      });
    }
    return new (B || (B = Promise))(function(ie, Ce) {
      function Oe(J) {
        try {
          W(N.next(J));
        } catch (Re) {
          Ce(Re);
        }
      }
      function Se(J) {
        try {
          W(N.throw(J));
        } catch (Re) {
          Ce(Re);
        }
      }
      function W(J) {
        J.done ? ie(J.value) : Y(J.value).then(Oe, Se);
      }
      W((N = N.apply(b, T || [])).next());
    });
  };
  let { value: s = "" } = e, { value_is_output: i = !1 } = e, { lines: f = 1 } = e, { placeholder: a = "Type here..." } = e, { label: r } = e, { info: o = void 0 } = e, { disabled: u = !1 } = e, { show_label: _ = !0 } = e, { container: d = !0 } = e, { max_lines: h } = e, { prompts: M = [] } = e, { suffixes: H = [] } = e, { type: k = "text" } = e, { rtl: Z = !1 } = e, { autofocus: c = !1 } = e, { text_align: m = void 0 } = e, { autoscroll: p = !0 } = e, V, w = !1, E, j = 0, R = !1;
  const D = oi();
  si(() => {
    E = V && V.offsetHeight + V.scrollTop > V.scrollHeight - 100;
  });
  const le = () => {
    E && p && !R && V.scrollTo(0, V.scrollHeight);
  };
  function ne() {
    D("change", s), i || D("input");
  }
  fi(() => {
    c && V.focus(), E && p && le(), t(21, i = !1);
  });
  function we() {
    return n(this, void 0, void 0, function* () {
      t(14, w = !w);
    });
  }
  function P(b) {
    t(0, s += `${b} `);
  }
  function de(b) {
    const T = b.target, B = T.value, N = [T.selectionStart, T.selectionEnd];
    D("select", { value: B.substring(...N), index: N });
  }
  function U(b) {
    return n(this, void 0, void 0, function* () {
      yield Mt(), (b.key === "Enter" && b.shiftKey && f > 1 || b.key === "Enter" && !b.shiftKey && f === 1 && h >= 1) && (b.preventDefault(), D("submit"));
    });
  }
  function ve(b) {
    const T = b.target, B = T.scrollTop;
    B < j && (R = !0), j = B;
    const N = T.scrollHeight - T.clientHeight;
    B >= N && (R = !1);
  }
  function he(b) {
    return n(this, void 0, void 0, function* () {
      if (yield Mt(), f === h)
        return;
      let T = h === void 0 ? !1 : h === void 0 ? 21 * 11 : 21 * (h + 1), B = 21 * (f + 1);
      const N = b.target;
      N.style.height = "1px";
      let Y;
      T && N.scrollHeight > T ? Y = T : N.scrollHeight < B ? Y = B : Y = N.scrollHeight, N.style.height = `${Y}px`;
    });
  }
  function ke(b, T) {
    if (f !== h && (b.style.overflowY = "scroll", b.addEventListener("input", he), !!T.trim()))
      return he({ target: b }), {
        destroy: () => b.removeEventListener("input", he)
      };
  }
  function g(b) {
    pt.call(this, l, b);
  }
  function pe(b) {
    pt.call(this, l, b);
  }
  function Ue() {
    s = this.value, t(0, s);
  }
  function Xe(b) {
    Wn[b ? "unshift" : "push"](() => {
      V = b, t(13, V);
    });
  }
  const Ge = (b) => P(b), v = (b) => P(b);
  return l.$$set = (b) => {
    "value" in b && t(0, s = b.value), "value_is_output" in b && t(21, i = b.value_is_output), "lines" in b && t(1, f = b.lines), "placeholder" in b && t(2, a = b.placeholder), "label" in b && t(3, r = b.label), "info" in b && t(4, o = b.info), "disabled" in b && t(5, u = b.disabled), "show_label" in b && t(6, _ = b.show_label), "container" in b && t(7, d = b.container), "max_lines" in b && t(22, h = b.max_lines), "prompts" in b && t(8, M = b.prompts), "suffixes" in b && t(9, H = b.suffixes), "type" in b && t(23, k = b.type), "rtl" in b && t(10, Z = b.rtl), "autofocus" in b && t(11, c = b.autofocus), "text_align" in b && t(12, m = b.text_align), "autoscroll" in b && t(24, p = b.autoscroll);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*value*/
    1 && s === null && t(0, s = ""), l.$$.dirty[0] & /*value, el, lines, max_lines*/
    4202499 && V && f !== h && he({ target: V }), l.$$.dirty[0] & /*value*/
    1 && ne();
  }, [
    s,
    f,
    a,
    r,
    o,
    u,
    _,
    d,
    M,
    H,
    Z,
    c,
    m,
    V,
    w,
    we,
    P,
    de,
    U,
    ve,
    ke,
    i,
    h,
    k,
    p,
    g,
    pe,
    Ue,
    Xe,
    Ge,
    v
  ];
}
class di extends Gn {
  constructor(e) {
    super(), ei(
      this,
      e,
      ci,
      _i,
      ii,
      {
        value: 0,
        value_is_output: 21,
        lines: 1,
        placeholder: 2,
        label: 3,
        info: 4,
        disabled: 5,
        show_label: 6,
        container: 7,
        max_lines: 22,
        prompts: 8,
        suffixes: 9,
        type: 23,
        rtl: 10,
        autofocus: 11,
        text_align: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
function qe(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
const {
  SvelteComponent: mi,
  append: x,
  attr: q,
  component_subscribe: zt,
  detach: hi,
  element: bi,
  init: gi,
  insert: wi,
  noop: Et,
  safe_not_equal: vi,
  set_style: Be,
  svg_element: $,
  toggle_class: Tt
} = window.__gradio__svelte__internal, { onMount: ki } = window.__gradio__svelte__internal;
function pi(l) {
  let e, t, n, s, i, f, a, r, o, u, _, d;
  return {
    c() {
      e = bi("div"), t = $("svg"), n = $("g"), s = $("path"), i = $("path"), f = $("path"), a = $("path"), r = $("g"), o = $("path"), u = $("path"), _ = $("path"), d = $("path"), q(s, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(s, "fill", "#FF7C00"), q(s, "fill-opacity", "0.4"), q(s, "class", "svelte-43sxxs"), q(i, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(i, "fill", "#FF7C00"), q(i, "class", "svelte-43sxxs"), q(f, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(f, "fill", "#FF7C00"), q(f, "fill-opacity", "0.4"), q(f, "class", "svelte-43sxxs"), q(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(a, "fill", "#FF7C00"), q(a, "class", "svelte-43sxxs"), Be(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(o, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(u, "fill", "#FF7C00"), q(u, "class", "svelte-43sxxs"), q(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(_, "fill", "#FF7C00"), q(_, "fill-opacity", "0.4"), q(_, "class", "svelte-43sxxs"), q(d, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(d, "fill", "#FF7C00"), q(d, "class", "svelte-43sxxs"), Be(r, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Tt(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(h, M) {
      wi(h, e, M), x(e, t), x(t, n), x(n, s), x(n, i), x(n, f), x(n, a), x(t, r), x(r, o), x(r, u), x(r, _), x(r, d);
    },
    p(h, [M]) {
      M & /*$top*/
      2 && Be(n, "transform", "translate(" + /*$top*/
      h[1][0] + "px, " + /*$top*/
      h[1][1] + "px)"), M & /*$bottom*/
      4 && Be(r, "transform", "translate(" + /*$bottom*/
      h[2][0] + "px, " + /*$bottom*/
      h[2][1] + "px)"), M & /*margin*/
      1 && Tt(
        e,
        "margin",
        /*margin*/
        h[0]
      );
    },
    i: Et,
    o: Et,
    d(h) {
      h && hi(e);
    }
  };
}
function Ci(l, e, t) {
  let n, s;
  var i = this && this.__awaiter || function(h, M, H, k) {
    function Z(c) {
      return c instanceof H ? c : new H(function(m) {
        m(c);
      });
    }
    return new (H || (H = Promise))(function(c, m) {
      function p(E) {
        try {
          w(k.next(E));
        } catch (j) {
          m(j);
        }
      }
      function V(E) {
        try {
          w(k.throw(E));
        } catch (j) {
          m(j);
        }
      }
      function w(E) {
        E.done ? c(E.value) : Z(E.value).then(p, V);
      }
      w((k = k.apply(h, M || [])).next());
    });
  };
  let { margin: f = !0 } = e;
  const a = kt([0, 0]);
  zt(l, a, (h) => t(1, n = h));
  const r = kt([0, 0]);
  zt(l, r, (h) => t(2, s = h));
  let o;
  function u() {
    return i(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 140]), r.set([-125, -140])]), yield Promise.all([a.set([-125, 140]), r.set([125, -140])]), yield Promise.all([a.set([-125, 0]), r.set([125, -0])]), yield Promise.all([a.set([125, 0]), r.set([-125, 0])]);
    });
  }
  function _() {
    return i(this, void 0, void 0, function* () {
      yield u(), o || _();
    });
  }
  function d() {
    return i(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 0]), r.set([-125, 0])]), _();
    });
  }
  return ki(() => (d(), () => o = !0)), l.$$set = (h) => {
    "margin" in h && t(0, f = h.margin);
  }, [f, n, s, a, r];
}
class yi extends mi {
  constructor(e) {
    super(), gi(this, e, Ci, pi, vi, { margin: 0 });
  }
}
const {
  SvelteComponent: Li,
  append: ge,
  attr: te,
  binding_callbacks: Bt,
  check_outros: it,
  create_component: ul,
  create_slot: _l,
  destroy_component: cl,
  destroy_each: dl,
  detach: y,
  element: ae,
  empty: Fe,
  ensure_array_like: Ke,
  get_all_dirty_from_scope: ml,
  get_slot_changes: hl,
  group_outros: st,
  init: Mi,
  insert: L,
  mount_component: bl,
  noop: ft,
  safe_not_equal: Vi,
  set_data: O,
  set_style: be,
  space: G,
  text: z,
  toggle_class: X,
  transition_in: ee,
  transition_out: re,
  update_slot_base: gl
} = window.__gradio__svelte__internal, { tick: qi } = window.__gradio__svelte__internal, { onDestroy: Hi } = window.__gradio__svelte__internal, { createEventDispatcher: Zi } = window.__gradio__svelte__internal, Fi = (l) => ({}), Nt = (l) => ({}), Si = (l) => ({}), Dt = (l) => ({});
function It(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function jt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function zi(l) {
  let e, t, n, s, i = (
    /*i18n*/
    l[1]("common.error") + ""
  ), f, a, r;
  t = new En({
    props: {
      Icon: An,
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
  const o = (
    /*#slots*/
    l[30].error
  ), u = _l(
    o,
    l,
    /*$$scope*/
    l[29],
    Nt
  );
  return {
    c() {
      e = ae("div"), ul(t.$$.fragment), n = G(), s = ae("span"), f = z(i), a = G(), u && u.c(), te(e, "class", "clear-status svelte-vopvsi"), te(s, "class", "error svelte-vopvsi");
    },
    m(_, d) {
      L(_, e, d), bl(t, e, null), L(_, n, d), L(_, s, d), ge(s, f), L(_, a, d), u && u.m(_, d), r = !0;
    },
    p(_, d) {
      const h = {};
      d[0] & /*i18n*/
      2 && (h.label = /*i18n*/
      _[1]("common.clear")), t.$set(h), (!r || d[0] & /*i18n*/
      2) && i !== (i = /*i18n*/
      _[1]("common.error") + "") && O(f, i), u && u.p && (!r || d[0] & /*$$scope*/
      536870912) && gl(
        u,
        o,
        _,
        /*$$scope*/
        _[29],
        r ? hl(
          o,
          /*$$scope*/
          _[29],
          d,
          Fi
        ) : ml(
          /*$$scope*/
          _[29]
        ),
        Nt
      );
    },
    i(_) {
      r || (ee(t.$$.fragment, _), ee(u, _), r = !0);
    },
    o(_) {
      re(t.$$.fragment, _), re(u, _), r = !1;
    },
    d(_) {
      _ && (y(e), y(n), y(s), y(a)), cl(t), u && u.d(_);
    }
  };
}
function Ei(l) {
  let e, t, n, s, i, f, a, r, o, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && At(l)
  );
  function _(m, p) {
    if (
      /*progress*/
      m[7]
    )
      return Ni;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return Bi;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return Ti;
  }
  let d = _(l), h = d && d(l), M = (
    /*timer*/
    l[5] && Kt(l)
  );
  const H = [Ai, ji], k = [];
  function Z(m, p) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(i = Z(l)) && (f = k[i] = H[i](l));
  let c = !/*timer*/
  l[5] && Jt(l);
  return {
    c() {
      u && u.c(), e = G(), t = ae("div"), h && h.c(), n = G(), M && M.c(), s = G(), f && f.c(), a = G(), c && c.c(), r = Fe(), te(t, "class", "progress-text svelte-vopvsi"), X(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), X(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(m, p) {
      u && u.m(m, p), L(m, e, p), L(m, t, p), h && h.m(t, null), ge(t, n), M && M.m(t, null), L(m, s, p), ~i && k[i].m(m, p), L(m, a, p), c && c.m(m, p), L(m, r, p), o = !0;
    },
    p(m, p) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? u ? u.p(m, p) : (u = At(m), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), d === (d = _(m)) && h ? h.p(m, p) : (h && h.d(1), h = d && d(m), h && (h.c(), h.m(t, n))), /*timer*/
      m[5] ? M ? M.p(m, p) : (M = Kt(m), M.c(), M.m(t, null)) : M && (M.d(1), M = null), (!o || p[0] & /*variant*/
      256) && X(
        t,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!o || p[0] & /*variant*/
      256) && X(
        t,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let V = i;
      i = Z(m), i === V ? ~i && k[i].p(m, p) : (f && (st(), re(k[V], 1, 1, () => {
        k[V] = null;
      }), it()), ~i ? (f = k[i], f ? f.p(m, p) : (f = k[i] = H[i](m), f.c()), ee(f, 1), f.m(a.parentNode, a)) : f = null), /*timer*/
      m[5] ? c && (st(), re(c, 1, 1, () => {
        c = null;
      }), it()) : c ? (c.p(m, p), p[0] & /*timer*/
      32 && ee(c, 1)) : (c = Jt(m), c.c(), ee(c, 1), c.m(r.parentNode, r));
    },
    i(m) {
      o || (ee(f), ee(c), o = !0);
    },
    o(m) {
      re(f), re(c), o = !1;
    },
    d(m) {
      m && (y(e), y(t), y(s), y(a), y(r)), u && u.d(m), h && h.d(), M && M.d(), ~i && k[i].d(m), c && c.d(m);
    }
  };
}
function At(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = ae("div"), te(e, "class", "eta-bar svelte-vopvsi"), be(e, "transform", t);
    },
    m(n, s) {
      L(n, e, s);
    },
    p(n, s) {
      s[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && be(e, "transform", t);
    },
    d(n) {
      n && y(e);
    }
  };
}
function Ti(l) {
  let e;
  return {
    c() {
      e = z("processing |");
    },
    m(t, n) {
      L(t, e, n);
    },
    p: ft,
    d(t) {
      t && y(e);
    }
  };
}
function Bi(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, s, i, f;
  return {
    c() {
      e = z("queue: "), n = z(t), s = z("/"), i = z(
        /*queue_size*/
        l[3]
      ), f = z(" |");
    },
    m(a, r) {
      L(a, e, r), L(a, n, r), L(a, s, r), L(a, i, r), L(a, f, r);
    },
    p(a, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      a[2] + 1 + "") && O(n, t), r[0] & /*queue_size*/
      8 && O(
        i,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (y(e), y(n), y(s), y(i), y(f));
    }
  };
}
function Ni(l) {
  let e, t = Ke(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = Yt(jt(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Fe();
    },
    m(s, i) {
      for (let f = 0; f < n.length; f += 1)
        n[f] && n[f].m(s, i);
      L(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress*/
      128) {
        t = Ke(
          /*progress*/
          s[7]
        );
        let f;
        for (f = 0; f < t.length; f += 1) {
          const a = jt(s, t, f);
          n[f] ? n[f].p(a, i) : (n[f] = Yt(a), n[f].c(), n[f].m(e.parentNode, e));
        }
        for (; f < n.length; f += 1)
          n[f].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && y(e), dl(n, s);
    }
  };
}
function Pt(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, s, i = " ", f;
  function a(u, _) {
    return (
      /*p*/
      u[41].length != null ? Ii : Di
    );
  }
  let r = a(l), o = r(l);
  return {
    c() {
      o.c(), e = G(), n = z(t), s = z(" | "), f = z(i);
    },
    m(u, _) {
      o.m(u, _), L(u, e, _), L(u, n, _), L(u, s, _), L(u, f, _);
    },
    p(u, _) {
      r === (r = a(u)) && o ? o.p(u, _) : (o.d(1), o = r(u), o && (o.c(), o.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && O(n, t);
    },
    d(u) {
      u && (y(e), y(n), y(s), y(f)), o.d(u);
    }
  };
}
function Di(l) {
  let e = qe(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      L(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = qe(
        /*p*/
        n[41].index || 0
      ) + "") && O(t, e);
    },
    d(n) {
      n && y(t);
    }
  };
}
function Ii(l) {
  let e = qe(
    /*p*/
    l[41].index || 0
  ) + "", t, n, s = qe(
    /*p*/
    l[41].length
  ) + "", i;
  return {
    c() {
      t = z(e), n = z("/"), i = z(s);
    },
    m(f, a) {
      L(f, t, a), L(f, n, a), L(f, i, a);
    },
    p(f, a) {
      a[0] & /*progress*/
      128 && e !== (e = qe(
        /*p*/
        f[41].index || 0
      ) + "") && O(t, e), a[0] & /*progress*/
      128 && s !== (s = qe(
        /*p*/
        f[41].length
      ) + "") && O(i, s);
    },
    d(f) {
      f && (y(t), y(n), y(i));
    }
  };
}
function Yt(l) {
  let e, t = (
    /*p*/
    l[41].index != null && Pt(l)
  );
  return {
    c() {
      t && t.c(), e = Fe();
    },
    m(n, s) {
      t && t.m(n, s), L(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].index != null ? t ? t.p(n, s) : (t = Pt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && y(e), t && t.d(n);
    }
  };
}
function Kt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, s;
  return {
    c() {
      e = z(
        /*formatted_timer*/
        l[20]
      ), n = z(t), s = z("s");
    },
    m(i, f) {
      L(i, e, f), L(i, n, f), L(i, s, f);
    },
    p(i, f) {
      f[0] & /*formatted_timer*/
      1048576 && O(
        e,
        /*formatted_timer*/
        i[20]
      ), f[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      i[0] ? `/${/*formatted_eta*/
      i[19]}` : "") && O(n, t);
    },
    d(i) {
      i && (y(e), y(n), y(s));
    }
  };
}
function ji(l) {
  let e, t;
  return e = new yi({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      ul(e.$$.fragment);
    },
    m(n, s) {
      bl(e, n, s), t = !0;
    },
    p(n, s) {
      const i = {};
      s[0] & /*variant*/
      256 && (i.margin = /*variant*/
      n[8] === "default"), e.$set(i);
    },
    i(n) {
      t || (ee(e.$$.fragment, n), t = !0);
    },
    o(n) {
      re(e.$$.fragment, n), t = !1;
    },
    d(n) {
      cl(e, n);
    }
  };
}
function Ai(l) {
  let e, t, n, s, i, f = `${/*last_progress_level*/
  l[15] * 100}%`, a = (
    /*progress*/
    l[7] != null && Ut(l)
  );
  return {
    c() {
      e = ae("div"), t = ae("div"), a && a.c(), n = G(), s = ae("div"), i = ae("div"), te(t, "class", "progress-level-inner svelte-vopvsi"), te(i, "class", "progress-bar svelte-vopvsi"), be(i, "width", f), te(s, "class", "progress-bar-wrap svelte-vopvsi"), te(e, "class", "progress-level svelte-vopvsi");
    },
    m(r, o) {
      L(r, e, o), ge(e, t), a && a.m(t, null), ge(e, n), ge(e, s), ge(s, i), l[31](i);
    },
    p(r, o) {
      /*progress*/
      r[7] != null ? a ? a.p(r, o) : (a = Ut(r), a.c(), a.m(t, null)) : a && (a.d(1), a = null), o[0] & /*last_progress_level*/
      32768 && f !== (f = `${/*last_progress_level*/
      r[15] * 100}%`) && be(i, "width", f);
    },
    i: ft,
    o: ft,
    d(r) {
      r && y(e), a && a.d(), l[31](null);
    }
  };
}
function Ut(l) {
  let e, t = Ke(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = Wt(It(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Fe();
    },
    m(s, i) {
      for (let f = 0; f < n.length; f += 1)
        n[f] && n[f].m(s, i);
      L(s, e, i);
    },
    p(s, i) {
      if (i[0] & /*progress_level, progress*/
      16512) {
        t = Ke(
          /*progress*/
          s[7]
        );
        let f;
        for (f = 0; f < t.length; f += 1) {
          const a = It(s, t, f);
          n[f] ? n[f].p(a, i) : (n[f] = Wt(a), n[f].c(), n[f].m(e.parentNode, e));
        }
        for (; f < n.length; f += 1)
          n[f].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && y(e), dl(n, s);
    }
  };
}
function Xt(l) {
  let e, t, n, s, i = (
    /*i*/
    l[43] !== 0 && Pi()
  ), f = (
    /*p*/
    l[41].desc != null && Gt(l)
  ), a = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && Ot()
  ), r = (
    /*progress_level*/
    l[14] != null && Rt(l)
  );
  return {
    c() {
      i && i.c(), e = G(), f && f.c(), t = G(), a && a.c(), n = G(), r && r.c(), s = Fe();
    },
    m(o, u) {
      i && i.m(o, u), L(o, e, u), f && f.m(o, u), L(o, t, u), a && a.m(o, u), L(o, n, u), r && r.m(o, u), L(o, s, u);
    },
    p(o, u) {
      /*p*/
      o[41].desc != null ? f ? f.p(o, u) : (f = Gt(o), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), /*p*/
      o[41].desc != null && /*progress_level*/
      o[14] && /*progress_level*/
      o[14][
        /*i*/
        o[43]
      ] != null ? a || (a = Ot(), a.c(), a.m(n.parentNode, n)) : a && (a.d(1), a = null), /*progress_level*/
      o[14] != null ? r ? r.p(o, u) : (r = Rt(o), r.c(), r.m(s.parentNode, s)) : r && (r.d(1), r = null);
    },
    d(o) {
      o && (y(e), y(t), y(n), y(s)), i && i.d(o), f && f.d(o), a && a.d(o), r && r.d(o);
    }
  };
}
function Pi(l) {
  let e;
  return {
    c() {
      e = z(" /");
    },
    m(t, n) {
      L(t, e, n);
    },
    d(t) {
      t && y(e);
    }
  };
}
function Gt(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      L(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && O(t, e);
    },
    d(n) {
      n && y(t);
    }
  };
}
function Ot(l) {
  let e;
  return {
    c() {
      e = z("-");
    },
    m(t, n) {
      L(t, e, n);
    },
    d(t) {
      t && y(e);
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
      t = z(e), n = z("%");
    },
    m(s, i) {
      L(s, t, i), L(s, n, i);
    },
    p(s, i) {
      i[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (s[14][
        /*i*/
        s[43]
      ] || 0)).toFixed(1) + "") && O(t, e);
    },
    d(s) {
      s && (y(t), y(n));
    }
  };
}
function Wt(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && Xt(l)
  );
  return {
    c() {
      t && t.c(), e = Fe();
    },
    m(n, s) {
      t && t.m(n, s), L(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, s) : (t = Xt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && y(e), t && t.d(n);
    }
  };
}
function Jt(l) {
  let e, t, n, s;
  const i = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), f = _l(
    i,
    l,
    /*$$scope*/
    l[29],
    Dt
  );
  return {
    c() {
      e = ae("p"), t = z(
        /*loading_text*/
        l[9]
      ), n = G(), f && f.c(), te(e, "class", "loading svelte-vopvsi");
    },
    m(a, r) {
      L(a, e, r), ge(e, t), L(a, n, r), f && f.m(a, r), s = !0;
    },
    p(a, r) {
      (!s || r[0] & /*loading_text*/
      512) && O(
        t,
        /*loading_text*/
        a[9]
      ), f && f.p && (!s || r[0] & /*$$scope*/
      536870912) && gl(
        f,
        i,
        a,
        /*$$scope*/
        a[29],
        s ? hl(
          i,
          /*$$scope*/
          a[29],
          r,
          Si
        ) : ml(
          /*$$scope*/
          a[29]
        ),
        Dt
      );
    },
    i(a) {
      s || (ee(f, a), s = !0);
    },
    o(a) {
      re(f, a), s = !1;
    },
    d(a) {
      a && (y(e), y(n)), f && f.d(a);
    }
  };
}
function Yi(l) {
  let e, t, n, s, i;
  const f = [Ei, zi], a = [];
  function r(o, u) {
    return (
      /*status*/
      o[4] === "pending" ? 0 : (
        /*status*/
        o[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(l)) && (n = a[t] = f[t](l)), {
    c() {
      e = ae("div"), n && n.c(), te(e, "class", s = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-vopvsi"), X(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), X(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), X(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), X(
        e,
        "border",
        /*border*/
        l[12]
      ), be(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), be(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(o, u) {
      L(o, e, u), ~t && a[t].m(e, null), l[33](e), i = !0;
    },
    p(o, u) {
      let _ = t;
      t = r(o), t === _ ? ~t && a[t].p(o, u) : (n && (st(), re(a[_], 1, 1, () => {
        a[_] = null;
      }), it()), ~t ? (n = a[t], n ? n.p(o, u) : (n = a[t] = f[t](o), n.c()), ee(n, 1), n.m(e, null)) : n = null), (!i || u[0] & /*variant, show_progress*/
      320 && s !== (s = "wrap " + /*variant*/
      o[8] + " " + /*show_progress*/
      o[6] + " svelte-vopvsi")) && te(e, "class", s), (!i || u[0] & /*variant, show_progress, status, show_progress*/
      336) && X(e, "hide", !/*status*/
      o[4] || /*status*/
      o[4] === "complete" || /*show_progress*/
      o[6] === "hidden"), (!i || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && X(
        e,
        "translucent",
        /*variant*/
        o[8] === "center" && /*status*/
        (o[4] === "pending" || /*status*/
        o[4] === "error") || /*translucent*/
        o[11] || /*show_progress*/
        o[6] === "minimal"
      ), (!i || u[0] & /*variant, show_progress, status*/
      336) && X(
        e,
        "generating",
        /*status*/
        o[4] === "generating"
      ), (!i || u[0] & /*variant, show_progress, border*/
      4416) && X(
        e,
        "border",
        /*border*/
        o[12]
      ), u[0] & /*absolute*/
      1024 && be(
        e,
        "position",
        /*absolute*/
        o[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && be(
        e,
        "padding",
        /*absolute*/
        o[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(o) {
      i || (ee(n), i = !0);
    },
    o(o) {
      re(n), i = !1;
    },
    d(o) {
      o && y(e), ~t && a[t].d(), l[33](null);
    }
  };
}
var Ki = function(l, e, t, n) {
  function s(i) {
    return i instanceof t ? i : new t(function(f) {
      f(i);
    });
  }
  return new (t || (t = Promise))(function(i, f) {
    function a(u) {
      try {
        o(n.next(u));
      } catch (_) {
        f(_);
      }
    }
    function r(u) {
      try {
        o(n.throw(u));
      } catch (_) {
        f(_);
      }
    }
    function o(u) {
      u.done ? i(u.value) : s(u.value).then(a, r);
    }
    o((n = n.apply(l, e || [])).next());
  });
};
let Ne = [], et = !1;
function Ui(l) {
  return Ki(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Ne.push(e), !et)
        et = !0;
      else
        return;
      yield qi(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let s = 0; s < Ne.length; s++) {
          const f = Ne[s].getBoundingClientRect();
          (s === 0 || f.top + window.scrollY <= n[0]) && (n[0] = f.top + window.scrollY, n[1] = s);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), et = !1, Ne = [];
      });
    }
  });
}
function Xi(l, e, t) {
  let n, { $$slots: s = {}, $$scope: i } = e;
  this && this.__awaiter;
  const f = Zi();
  let { i18n: a } = e, { eta: r = null } = e, { queue_position: o } = e, { queue_size: u } = e, { status: _ } = e, { scroll_to_output: d = !1 } = e, { timer: h = !0 } = e, { show_progress: M = "full" } = e, { message: H = null } = e, { progress: k = null } = e, { variant: Z = "default" } = e, { loading_text: c = "Loading..." } = e, { absolute: m = !0 } = e, { translucent: p = !1 } = e, { border: V = !1 } = e, { autoscroll: w } = e, E, j = !1, R = 0, D = 0, le = null, ne = null, we = 0, P = null, de, U = null, ve = !0;
  const he = () => {
    t(0, r = t(27, le = t(19, pe = null))), t(25, R = performance.now()), t(26, D = 0), j = !0, ke();
  };
  function ke() {
    requestAnimationFrame(() => {
      t(26, D = (performance.now() - R) / 1e3), j && ke();
    });
  }
  function g() {
    t(26, D = 0), t(0, r = t(27, le = t(19, pe = null))), j && (j = !1);
  }
  Hi(() => {
    j && g();
  });
  let pe = null;
  function Ue(v) {
    Bt[v ? "unshift" : "push"](() => {
      U = v, t(16, U), t(7, k), t(14, P), t(15, de);
    });
  }
  const Xe = () => {
    f("clear_status");
  };
  function Ge(v) {
    Bt[v ? "unshift" : "push"](() => {
      E = v, t(13, E);
    });
  }
  return l.$$set = (v) => {
    "i18n" in v && t(1, a = v.i18n), "eta" in v && t(0, r = v.eta), "queue_position" in v && t(2, o = v.queue_position), "queue_size" in v && t(3, u = v.queue_size), "status" in v && t(4, _ = v.status), "scroll_to_output" in v && t(22, d = v.scroll_to_output), "timer" in v && t(5, h = v.timer), "show_progress" in v && t(6, M = v.show_progress), "message" in v && t(23, H = v.message), "progress" in v && t(7, k = v.progress), "variant" in v && t(8, Z = v.variant), "loading_text" in v && t(9, c = v.loading_text), "absolute" in v && t(10, m = v.absolute), "translucent" in v && t(11, p = v.translucent), "border" in v && t(12, V = v.border), "autoscroll" in v && t(24, w = v.autoscroll), "$$scope" in v && t(29, i = v.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (r === null && t(0, r = le), r != null && le !== r && (t(28, ne = (performance.now() - R) / 1e3 + r), t(19, pe = ne.toFixed(1)), t(27, le = r))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, we = ne === null || ne <= 0 || !D ? null : Math.min(D / ne, 1)), l.$$.dirty[0] & /*progress*/
    128 && k != null && t(18, ve = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (k != null ? t(14, P = k.map((v) => {
      if (v.index != null && v.length != null)
        return v.index / v.length;
      if (v.progress != null)
        return v.progress;
    })) : t(14, P = null), P ? (t(15, de = P[P.length - 1]), U && (de === 0 ? t(16, U.style.transition = "0", U) : t(16, U.style.transition = "150ms", U))) : t(15, de = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? he() : g()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && E && d && (_ === "pending" || _ === "complete") && Ui(E, w), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = D.toFixed(1));
  }, [
    r,
    a,
    o,
    u,
    _,
    h,
    M,
    k,
    Z,
    c,
    m,
    p,
    V,
    E,
    P,
    de,
    U,
    we,
    ve,
    pe,
    n,
    f,
    d,
    H,
    w,
    R,
    D,
    le,
    ne,
    i,
    s,
    Ue,
    Xe,
    Ge
  ];
}
class Gi extends Li {
  constructor(e) {
    super(), Mi(
      this,
      e,
      Xi,
      Yi,
      Vi,
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
  SvelteComponent: Oi,
  add_iframe_resize_listener: Ri,
  add_render_callback: Wi,
  append: Ji,
  attr: Qi,
  binding_callbacks: xi,
  detach: $i,
  element: es,
  init: ts,
  insert: ls,
  noop: Qt,
  safe_not_equal: ns,
  set_data: is,
  text: ss,
  toggle_class: Ve
} = window.__gradio__svelte__internal, { onMount: fs } = window.__gradio__svelte__internal;
function os(l) {
  let e, t = (
    /*value*/
    (l[0] ? (
      /*value*/
      l[0]
    ) : "") + ""
  ), n, s;
  return {
    c() {
      e = es("div"), n = ss(t), Qi(e, "class", "svelte-84cxb8"), Wi(() => (
        /*div_elementresize_handler*/
        l[5].call(e)
      )), Ve(
        e,
        "table",
        /*type*/
        l[1] === "table"
      ), Ve(
        e,
        "gallery",
        /*type*/
        l[1] === "gallery"
      ), Ve(
        e,
        "selected",
        /*selected*/
        l[2]
      );
    },
    m(i, f) {
      ls(i, e, f), Ji(e, n), s = Ri(
        e,
        /*div_elementresize_handler*/
        l[5].bind(e)
      ), l[6](e);
    },
    p(i, [f]) {
      f & /*value*/
      1 && t !== (t = /*value*/
      (i[0] ? (
        /*value*/
        i[0]
      ) : "") + "") && is(n, t), f & /*type*/
      2 && Ve(
        e,
        "table",
        /*type*/
        i[1] === "table"
      ), f & /*type*/
      2 && Ve(
        e,
        "gallery",
        /*type*/
        i[1] === "gallery"
      ), f & /*selected*/
      4 && Ve(
        e,
        "selected",
        /*selected*/
        i[2]
      );
    },
    i: Qt,
    o: Qt,
    d(i) {
      i && $i(e), s(), l[6](null);
    }
  };
}
function as(l, e, t) {
  let { value: n } = e, { type: s } = e, { selected: i = !1 } = e, f, a;
  function r(_, d) {
    !_ || !d || (a.style.setProperty("--local-text-width", `${d < 150 ? d : 200}px`), t(4, a.style.whiteSpace = "unset", a));
  }
  fs(() => {
    r(a, f);
  });
  function o() {
    f = this.clientWidth, t(3, f);
  }
  function u(_) {
    xi[_ ? "unshift" : "push"](() => {
      a = _, t(4, a);
    });
  }
  return l.$$set = (_) => {
    "value" in _ && t(0, n = _.value), "type" in _ && t(1, s = _.type), "selected" in _ && t(2, i = _.selected);
  }, [n, s, i, f, a, o, u];
}
class ys extends Oi {
  constructor(e) {
    super(), ts(this, e, as, os, ns, { value: 0, type: 1, selected: 2 });
  }
}
const {
  SvelteComponent: rs,
  add_flush_callback: xt,
  assign: us,
  bind: $t,
  binding_callbacks: el,
  check_outros: _s,
  create_component: rt,
  destroy_component: ut,
  detach: cs,
  flush: F,
  get_spread_object: ds,
  get_spread_update: ms,
  group_outros: hs,
  init: bs,
  insert: gs,
  mount_component: _t,
  safe_not_equal: ws,
  space: vs,
  transition_in: He,
  transition_out: Ee
} = window.__gradio__svelte__internal;
function tl(l) {
  let e, t;
  const n = [
    { autoscroll: (
      /*gradio*/
      l[2].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[2].i18n
    ) },
    /*loading_status*/
    l[18]
  ];
  let s = {};
  for (let i = 0; i < n.length; i += 1)
    s = us(s, n[i]);
  return e = new Gi({ props: s }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[24]
  ), {
    c() {
      rt(e.$$.fragment);
    },
    m(i, f) {
      _t(e, i, f), t = !0;
    },
    p(i, f) {
      const a = f[0] & /*gradio, loading_status*/
      262148 ? ms(n, [
        f[0] & /*gradio*/
        4 && { autoscroll: (
          /*gradio*/
          i[2].autoscroll
        ) },
        f[0] & /*gradio*/
        4 && { i18n: (
          /*gradio*/
          i[2].i18n
        ) },
        f[0] & /*loading_status*/
        262144 && ds(
          /*loading_status*/
          i[18]
        )
      ]) : {};
      e.$set(a);
    },
    i(i) {
      t || (He(e.$$.fragment, i), t = !0);
    },
    o(i) {
      Ee(e.$$.fragment, i), t = !1;
    },
    d(i) {
      ut(e, i);
    }
  };
}
function ks(l) {
  let e, t, n, s, i, f = (
    /*loading_status*/
    l[18] && tl(l)
  );
  function a(u) {
    l[25](u);
  }
  function r(u) {
    l[26](u);
  }
  let o = {
    label: (
      /*label*/
      l[3]
    ),
    info: (
      /*info*/
      l[4]
    ),
    show_label: (
      /*show_label*/
      l[10]
    ),
    lines: (
      /*lines*/
      l[8]
    ),
    type: (
      /*type*/
      l[14]
    ),
    rtl: (
      /*rtl*/
      l[19]
    ),
    text_align: (
      /*text_align*/
      l[20]
    ),
    max_lines: /*max_lines*/ l[11] ? (
      /*max_lines*/
      l[11]
    ) : (
      /*lines*/
      l[8] + 1
    ),
    prompts: (
      /*prompts*/
      l[12]
    ),
    suffixes: (
      /*suffixes*/
      l[13]
    ),
    placeholder: (
      /*placeholder*/
      l[9]
    ),
    autofocus: (
      /*autofocus*/
      l[21]
    ),
    container: (
      /*container*/
      l[15]
    ),
    autoscroll: (
      /*autoscroll*/
      l[22]
    ),
    disabled: !/*interactive*/
    l[23]
  };
  return (
    /*value*/
    l[0] !== void 0 && (o.value = /*value*/
    l[0]), /*value_is_output*/
    l[1] !== void 0 && (o.value_is_output = /*value_is_output*/
    l[1]), t = new di({ props: o }), el.push(() => $t(t, "value", a)), el.push(() => $t(t, "value_is_output", r)), t.$on(
      "change",
      /*change_handler*/
      l[27]
    ), t.$on(
      "input",
      /*input_handler*/
      l[28]
    ), t.$on(
      "submit",
      /*submit_handler*/
      l[29]
    ), t.$on(
      "blur",
      /*blur_handler*/
      l[30]
    ), t.$on(
      "select",
      /*select_handler*/
      l[31]
    ), t.$on(
      "focus",
      /*focus_handler*/
      l[32]
    ), {
      c() {
        f && f.c(), e = vs(), rt(t.$$.fragment);
      },
      m(u, _) {
        f && f.m(u, _), gs(u, e, _), _t(t, u, _), i = !0;
      },
      p(u, _) {
        /*loading_status*/
        u[18] ? f ? (f.p(u, _), _[0] & /*loading_status*/
        262144 && He(f, 1)) : (f = tl(u), f.c(), He(f, 1), f.m(e.parentNode, e)) : f && (hs(), Ee(f, 1, 1, () => {
          f = null;
        }), _s());
        const d = {};
        _[0] & /*label*/
        8 && (d.label = /*label*/
        u[3]), _[0] & /*info*/
        16 && (d.info = /*info*/
        u[4]), _[0] & /*show_label*/
        1024 && (d.show_label = /*show_label*/
        u[10]), _[0] & /*lines*/
        256 && (d.lines = /*lines*/
        u[8]), _[0] & /*type*/
        16384 && (d.type = /*type*/
        u[14]), _[0] & /*rtl*/
        524288 && (d.rtl = /*rtl*/
        u[19]), _[0] & /*text_align*/
        1048576 && (d.text_align = /*text_align*/
        u[20]), _[0] & /*max_lines, lines*/
        2304 && (d.max_lines = /*max_lines*/
        u[11] ? (
          /*max_lines*/
          u[11]
        ) : (
          /*lines*/
          u[8] + 1
        )), _[0] & /*prompts*/
        4096 && (d.prompts = /*prompts*/
        u[12]), _[0] & /*suffixes*/
        8192 && (d.suffixes = /*suffixes*/
        u[13]), _[0] & /*placeholder*/
        512 && (d.placeholder = /*placeholder*/
        u[9]), _[0] & /*autofocus*/
        2097152 && (d.autofocus = /*autofocus*/
        u[21]), _[0] & /*container*/
        32768 && (d.container = /*container*/
        u[15]), _[0] & /*autoscroll*/
        4194304 && (d.autoscroll = /*autoscroll*/
        u[22]), _[0] & /*interactive*/
        8388608 && (d.disabled = !/*interactive*/
        u[23]), !n && _[0] & /*value*/
        1 && (n = !0, d.value = /*value*/
        u[0], xt(() => n = !1)), !s && _[0] & /*value_is_output*/
        2 && (s = !0, d.value_is_output = /*value_is_output*/
        u[1], xt(() => s = !1)), t.$set(d);
      },
      i(u) {
        i || (He(f), He(t.$$.fragment, u), i = !0);
      },
      o(u) {
        Ee(f), Ee(t.$$.fragment, u), i = !1;
      },
      d(u) {
        u && cs(e), f && f.d(u), ut(t, u);
      }
    }
  );
}
function ps(l) {
  let e, t;
  return e = new El({
    props: {
      visible: (
        /*visible*/
        l[7]
      ),
      elem_id: (
        /*elem_id*/
        l[5]
      ),
      elem_classes: (
        /*elem_classes*/
        l[6]
      ),
      scale: (
        /*scale*/
        l[16]
      ),
      min_width: (
        /*min_width*/
        l[17]
      ),
      allow_overflow: !1,
      padding: (
        /*container*/
        l[15]
      ),
      $$slots: { default: [ks] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      rt(e.$$.fragment);
    },
    m(n, s) {
      _t(e, n, s), t = !0;
    },
    p(n, s) {
      const i = {};
      s[0] & /*visible*/
      128 && (i.visible = /*visible*/
      n[7]), s[0] & /*elem_id*/
      32 && (i.elem_id = /*elem_id*/
      n[5]), s[0] & /*elem_classes*/
      64 && (i.elem_classes = /*elem_classes*/
      n[6]), s[0] & /*scale*/
      65536 && (i.scale = /*scale*/
      n[16]), s[0] & /*min_width*/
      131072 && (i.min_width = /*min_width*/
      n[17]), s[0] & /*container*/
      32768 && (i.padding = /*container*/
      n[15]), s[0] & /*label, info, show_label, lines, type, rtl, text_align, max_lines, prompts, suffixes, placeholder, autofocus, container, autoscroll, interactive, value, value_is_output, gradio, loading_status*/
      16580383 | s[1] & /*$$scope*/
      4 && (i.$$scope = { dirty: s, ctx: n }), e.$set(i);
    },
    i(n) {
      t || (He(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ee(e.$$.fragment, n), t = !1;
    },
    d(n) {
      ut(e, n);
    }
  };
}
function Cs(l, e, t) {
  let { gradio: n } = e, { label: s = "Textbox" } = e, { info: i = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: a = [] } = e, { visible: r = !0 } = e, { value: o = "" } = e, { lines: u } = e, { placeholder: _ = "" } = e, { show_label: d } = e, { max_lines: h } = e, { prompts: M = [] } = e, { suffixes: H = [] } = e, { type: k = "text" } = e, { container: Z = !0 } = e, { scale: c = null } = e, { min_width: m = void 0 } = e, { loading_status: p = void 0 } = e, { value_is_output: V = !1 } = e, { rtl: w = !1 } = e, { text_align: E = void 0 } = e, { autofocus: j = !1 } = e, { autoscroll: R = !0 } = e, { interactive: D } = e;
  const le = () => n.dispatch("clear_status", p);
  function ne(g) {
    o = g, t(0, o);
  }
  function we(g) {
    V = g, t(1, V);
  }
  const P = () => n.dispatch("change", o), de = () => n.dispatch("input"), U = () => n.dispatch("submit"), ve = () => n.dispatch("blur"), he = (g) => n.dispatch("select", g.detail), ke = () => n.dispatch("focus");
  return l.$$set = (g) => {
    "gradio" in g && t(2, n = g.gradio), "label" in g && t(3, s = g.label), "info" in g && t(4, i = g.info), "elem_id" in g && t(5, f = g.elem_id), "elem_classes" in g && t(6, a = g.elem_classes), "visible" in g && t(7, r = g.visible), "value" in g && t(0, o = g.value), "lines" in g && t(8, u = g.lines), "placeholder" in g && t(9, _ = g.placeholder), "show_label" in g && t(10, d = g.show_label), "max_lines" in g && t(11, h = g.max_lines), "prompts" in g && t(12, M = g.prompts), "suffixes" in g && t(13, H = g.suffixes), "type" in g && t(14, k = g.type), "container" in g && t(15, Z = g.container), "scale" in g && t(16, c = g.scale), "min_width" in g && t(17, m = g.min_width), "loading_status" in g && t(18, p = g.loading_status), "value_is_output" in g && t(1, V = g.value_is_output), "rtl" in g && t(19, w = g.rtl), "text_align" in g && t(20, E = g.text_align), "autofocus" in g && t(21, j = g.autofocus), "autoscroll" in g && t(22, R = g.autoscroll), "interactive" in g && t(23, D = g.interactive);
  }, [
    o,
    V,
    n,
    s,
    i,
    f,
    a,
    r,
    u,
    _,
    d,
    h,
    M,
    H,
    k,
    Z,
    c,
    m,
    p,
    w,
    E,
    j,
    R,
    D,
    le,
    ne,
    we,
    P,
    de,
    U,
    ve,
    he,
    ke
  ];
}
class Ls extends rs {
  constructor(e) {
    super(), bs(
      this,
      e,
      Cs,
      ps,
      ws,
      {
        gradio: 2,
        label: 3,
        info: 4,
        elem_id: 5,
        elem_classes: 6,
        visible: 7,
        value: 0,
        lines: 8,
        placeholder: 9,
        show_label: 10,
        max_lines: 11,
        prompts: 12,
        suffixes: 13,
        type: 14,
        container: 15,
        scale: 16,
        min_width: 17,
        loading_status: 18,
        value_is_output: 1,
        rtl: 19,
        text_align: 20,
        autofocus: 21,
        autoscroll: 22,
        interactive: 23
      },
      null,
      [-1, -1]
    );
  }
  get gradio() {
    return this.$$.ctx[2];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), F();
  }
  get label() {
    return this.$$.ctx[3];
  }
  set label(e) {
    this.$$set({ label: e }), F();
  }
  get info() {
    return this.$$.ctx[4];
  }
  set info(e) {
    this.$$set({ info: e }), F();
  }
  get elem_id() {
    return this.$$.ctx[5];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), F();
  }
  get elem_classes() {
    return this.$$.ctx[6];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), F();
  }
  get visible() {
    return this.$$.ctx[7];
  }
  set visible(e) {
    this.$$set({ visible: e }), F();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), F();
  }
  get lines() {
    return this.$$.ctx[8];
  }
  set lines(e) {
    this.$$set({ lines: e }), F();
  }
  get placeholder() {
    return this.$$.ctx[9];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), F();
  }
  get show_label() {
    return this.$$.ctx[10];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), F();
  }
  get max_lines() {
    return this.$$.ctx[11];
  }
  set max_lines(e) {
    this.$$set({ max_lines: e }), F();
  }
  get prompts() {
    return this.$$.ctx[12];
  }
  set prompts(e) {
    this.$$set({ prompts: e }), F();
  }
  get suffixes() {
    return this.$$.ctx[13];
  }
  set suffixes(e) {
    this.$$set({ suffixes: e }), F();
  }
  get type() {
    return this.$$.ctx[14];
  }
  set type(e) {
    this.$$set({ type: e }), F();
  }
  get container() {
    return this.$$.ctx[15];
  }
  set container(e) {
    this.$$set({ container: e }), F();
  }
  get scale() {
    return this.$$.ctx[16];
  }
  set scale(e) {
    this.$$set({ scale: e }), F();
  }
  get min_width() {
    return this.$$.ctx[17];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), F();
  }
  get loading_status() {
    return this.$$.ctx[18];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), F();
  }
  get value_is_output() {
    return this.$$.ctx[1];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), F();
  }
  get rtl() {
    return this.$$.ctx[19];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), F();
  }
  get text_align() {
    return this.$$.ctx[20];
  }
  set text_align(e) {
    this.$$set({ text_align: e }), F();
  }
  get autofocus() {
    return this.$$.ctx[21];
  }
  set autofocus(e) {
    this.$$set({ autofocus: e }), F();
  }
  get autoscroll() {
    return this.$$.ctx[22];
  }
  set autoscroll(e) {
    this.$$set({ autoscroll: e }), F();
  }
  get interactive() {
    return this.$$.ctx[23];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), F();
  }
}
export {
  ys as BaseExample,
  di as BaseTextbox,
  Ls as default
};
