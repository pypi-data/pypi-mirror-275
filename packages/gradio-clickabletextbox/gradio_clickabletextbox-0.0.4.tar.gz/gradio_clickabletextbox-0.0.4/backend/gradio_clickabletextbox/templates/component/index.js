const {
  SvelteComponent: Zl,
  assign: Sl,
  create_slot: zl,
  detach: El,
  element: Tl,
  get_all_dirty_from_scope: Bl,
  get_slot_changes: Nl,
  get_spread_update: Dl,
  init: Il,
  insert: jl,
  safe_not_equal: Al,
  set_dynamic_element_data: Lt,
  set_style: K,
  toggle_class: se,
  transition_in: cl,
  transition_out: dl,
  update_slot_base: Pl
} = window.__gradio__svelte__internal;
function Yl(l) {
  let e, t, n;
  const s = (
    /*#slots*/
    l[18].default
  ), f = zl(
    s,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let i = [
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
  ], o = {};
  for (let u = 0; u < i.length; u += 1)
    o = Sl(o, i[u]);
  return {
    c() {
      e = Tl(
        /*tag*/
        l[14]
      ), f && f.c(), Lt(
        /*tag*/
        l[14]
      )(e, o), se(
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
    m(u, a) {
      jl(u, e, a), f && f.m(e, null), n = !0;
    },
    p(u, a) {
      f && f.p && (!n || a & /*$$scope*/
      131072) && Pl(
        f,
        s,
        u,
        /*$$scope*/
        u[17],
        n ? Nl(
          s,
          /*$$scope*/
          u[17],
          a,
          null
        ) : Bl(
          /*$$scope*/
          u[17]
        ),
        null
      ), Lt(
        /*tag*/
        u[14]
      )(e, o = Dl(i, [
        (!n || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          u[7]
        ) },
        (!n || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          u[2]
        ) },
        (!n || a & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        u[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), se(
        e,
        "hidden",
        /*visible*/
        u[10] === !1
      ), se(
        e,
        "padded",
        /*padding*/
        u[6]
      ), se(
        e,
        "border_focus",
        /*border_mode*/
        u[5] === "focus"
      ), se(
        e,
        "border_contrast",
        /*border_mode*/
        u[5] === "contrast"
      ), se(e, "hide-container", !/*explicit_call*/
      u[8] && !/*container*/
      u[9]), a & /*height*/
      1 && K(
        e,
        "height",
        /*get_dimension*/
        u[15](
          /*height*/
          u[0]
        )
      ), a & /*width*/
      2 && K(e, "width", typeof /*width*/
      u[1] == "number" ? `calc(min(${/*width*/
      u[1]}px, 100%))` : (
        /*get_dimension*/
        u[15](
          /*width*/
          u[1]
        )
      )), a & /*variant*/
      16 && K(
        e,
        "border-style",
        /*variant*/
        u[4]
      ), a & /*allow_overflow*/
      2048 && K(
        e,
        "overflow",
        /*allow_overflow*/
        u[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && K(
        e,
        "flex-grow",
        /*scale*/
        u[12]
      ), a & /*min_width*/
      8192 && K(e, "min-width", `calc(min(${/*min_width*/
      u[13]}px, 100%))`);
    },
    i(u) {
      n || (cl(f, u), n = !0);
    },
    o(u) {
      dl(f, u), n = !1;
    },
    d(u) {
      u && El(e), f && f.d(u);
    }
  };
}
function Kl(l) {
  let e, t = (
    /*tag*/
    l[14] && Yl(l)
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
      e || (cl(t, n), e = !0);
    },
    o(n) {
      dl(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function Ol(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { height: f = void 0 } = e, { width: i = void 0 } = e, { elem_id: o = "" } = e, { elem_classes: u = [] } = e, { variant: a = "solid" } = e, { border_mode: r = "base" } = e, { padding: _ = !0 } = e, { type: c = "normal" } = e, { test_id: h = void 0 } = e, { explicit_call: L = !1 } = e, { container: M = !0 } = e, { visible: k = !0 } = e, { allow_overflow: v = !0 } = e, { scale: m = null } = e, { min_width: b = 0 } = e, C = c === "fieldset" ? "fieldset" : "div";
  const T = (p) => {
    if (p !== void 0) {
      if (typeof p == "number")
        return p + "px";
      if (typeof p == "string")
        return p;
    }
  };
  return l.$$set = (p) => {
    "height" in p && t(0, f = p.height), "width" in p && t(1, i = p.width), "elem_id" in p && t(2, o = p.elem_id), "elem_classes" in p && t(3, u = p.elem_classes), "variant" in p && t(4, a = p.variant), "border_mode" in p && t(5, r = p.border_mode), "padding" in p && t(6, _ = p.padding), "type" in p && t(16, c = p.type), "test_id" in p && t(7, h = p.test_id), "explicit_call" in p && t(8, L = p.explicit_call), "container" in p && t(9, M = p.container), "visible" in p && t(10, k = p.visible), "allow_overflow" in p && t(11, v = p.allow_overflow), "scale" in p && t(12, m = p.scale), "min_width" in p && t(13, b = p.min_width), "$$scope" in p && t(17, s = p.$$scope);
  }, [
    f,
    i,
    o,
    u,
    a,
    r,
    _,
    h,
    L,
    M,
    k,
    v,
    m,
    b,
    C,
    T,
    c,
    s,
    n
  ];
}
class Ul extends Zl {
  constructor(e) {
    super(), Il(this, e, Ol, Kl, Al, {
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
  SvelteComponent: Xl,
  attr: Gl,
  create_slot: Rl,
  detach: Wl,
  element: Jl,
  get_all_dirty_from_scope: Ql,
  get_slot_changes: xl,
  init: $l,
  insert: en,
  safe_not_equal: tn,
  transition_in: ln,
  transition_out: nn,
  update_slot_base: sn
} = window.__gradio__svelte__internal;
function fn(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[1].default
  ), s = Rl(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      e = Jl("div"), s && s.c(), Gl(e, "class", "svelte-1hnfib2");
    },
    m(f, i) {
      en(f, e, i), s && s.m(e, null), t = !0;
    },
    p(f, [i]) {
      s && s.p && (!t || i & /*$$scope*/
      1) && sn(
        s,
        n,
        f,
        /*$$scope*/
        f[0],
        t ? xl(
          n,
          /*$$scope*/
          f[0],
          i,
          null
        ) : Ql(
          /*$$scope*/
          f[0]
        ),
        null
      );
    },
    i(f) {
      t || (ln(s, f), t = !0);
    },
    o(f) {
      nn(s, f), t = !1;
    },
    d(f) {
      f && Wl(e), s && s.d(f);
    }
  };
}
function on(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e;
  return l.$$set = (f) => {
    "$$scope" in f && t(0, s = f.$$scope);
  }, [s, n];
}
class an extends Xl {
  constructor(e) {
    super(), $l(this, e, on, fn, tn, {});
  }
}
const {
  SvelteComponent: un,
  attr: Mt,
  check_outros: rn,
  create_component: _n,
  create_slot: cn,
  destroy_component: dn,
  detach: Pe,
  element: mn,
  empty: hn,
  get_all_dirty_from_scope: bn,
  get_slot_changes: gn,
  group_outros: wn,
  init: vn,
  insert: Ye,
  mount_component: pn,
  safe_not_equal: kn,
  set_data: Cn,
  space: yn,
  text: Ln,
  toggle_class: Le,
  transition_in: Be,
  transition_out: Ke,
  update_slot_base: Mn
} = window.__gradio__svelte__internal;
function Vt(l) {
  let e, t;
  return e = new an({
    props: {
      $$slots: { default: [Vn] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      _n(e.$$.fragment);
    },
    m(n, s) {
      pn(e, n, s), t = !0;
    },
    p(n, s) {
      const f = {};
      s & /*$$scope, info*/
      10 && (f.$$scope = { dirty: s, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (Be(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ke(e.$$.fragment, n), t = !1;
    },
    d(n) {
      dn(e, n);
    }
  };
}
function Vn(l) {
  let e;
  return {
    c() {
      e = Ln(
        /*info*/
        l[1]
      );
    },
    m(t, n) {
      Ye(t, e, n);
    },
    p(t, n) {
      n & /*info*/
      2 && Cn(
        e,
        /*info*/
        t[1]
      );
    },
    d(t) {
      t && Pe(e);
    }
  };
}
function Hn(l) {
  let e, t, n, s;
  const f = (
    /*#slots*/
    l[2].default
  ), i = cn(
    f,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let o = (
    /*info*/
    l[1] && Vt(l)
  );
  return {
    c() {
      e = mn("span"), i && i.c(), t = yn(), o && o.c(), n = hn(), Mt(e, "data-testid", "block-info"), Mt(e, "class", "svelte-22c38v"), Le(e, "sr-only", !/*show_label*/
      l[0]), Le(e, "hide", !/*show_label*/
      l[0]), Le(
        e,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(u, a) {
      Ye(u, e, a), i && i.m(e, null), Ye(u, t, a), o && o.m(u, a), Ye(u, n, a), s = !0;
    },
    p(u, [a]) {
      i && i.p && (!s || a & /*$$scope*/
      8) && Mn(
        i,
        f,
        u,
        /*$$scope*/
        u[3],
        s ? gn(
          f,
          /*$$scope*/
          u[3],
          a,
          null
        ) : bn(
          /*$$scope*/
          u[3]
        ),
        null
      ), (!s || a & /*show_label*/
      1) && Le(e, "sr-only", !/*show_label*/
      u[0]), (!s || a & /*show_label*/
      1) && Le(e, "hide", !/*show_label*/
      u[0]), (!s || a & /*info*/
      2) && Le(
        e,
        "has-info",
        /*info*/
        u[1] != null
      ), /*info*/
      u[1] ? o ? (o.p(u, a), a & /*info*/
      2 && Be(o, 1)) : (o = Vt(u), o.c(), Be(o, 1), o.m(n.parentNode, n)) : o && (wn(), Ke(o, 1, 1, () => {
        o = null;
      }), rn());
    },
    i(u) {
      s || (Be(i, u), Be(o), s = !0);
    },
    o(u) {
      Ke(i, u), Ke(o), s = !1;
    },
    d(u) {
      u && (Pe(e), Pe(t), Pe(n)), i && i.d(u), o && o.d(u);
    }
  };
}
function qn(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { show_label: f = !0 } = e, { info: i = void 0 } = e;
  return l.$$set = (o) => {
    "show_label" in o && t(0, f = o.show_label), "info" in o && t(1, i = o.info), "$$scope" in o && t(3, s = o.$$scope);
  }, [f, i, n, s];
}
class Fn extends un {
  constructor(e) {
    super(), vn(this, e, qn, Hn, kn, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: Zn,
  append: rt,
  attr: re,
  bubble: Sn,
  create_component: zn,
  destroy_component: En,
  detach: ml,
  element: _t,
  init: Tn,
  insert: hl,
  listen: Bn,
  mount_component: Nn,
  safe_not_equal: Dn,
  set_data: In,
  set_style: Me,
  space: jn,
  text: An,
  toggle_class: P,
  transition_in: Pn,
  transition_out: Yn
} = window.__gradio__svelte__internal;
function Ht(l) {
  let e, t;
  return {
    c() {
      e = _t("span"), t = An(
        /*label*/
        l[1]
      ), re(e, "class", "svelte-1lrphxw");
    },
    m(n, s) {
      hl(n, e, s), rt(e, t);
    },
    p(n, s) {
      s & /*label*/
      2 && In(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && ml(e);
    }
  };
}
function Kn(l) {
  let e, t, n, s, f, i, o, u = (
    /*show_label*/
    l[2] && Ht(l)
  );
  return s = new /*Icon*/
  l[0]({}), {
    c() {
      e = _t("button"), u && u.c(), t = jn(), n = _t("div"), zn(s.$$.fragment), re(n, "class", "svelte-1lrphxw"), P(
        n,
        "small",
        /*size*/
        l[4] === "small"
      ), P(
        n,
        "large",
        /*size*/
        l[4] === "large"
      ), P(
        n,
        "medium",
        /*size*/
        l[4] === "medium"
      ), e.disabled = /*disabled*/
      l[7], re(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), re(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), re(
        e,
        "title",
        /*label*/
        l[1]
      ), re(e, "class", "svelte-1lrphxw"), P(
        e,
        "pending",
        /*pending*/
        l[3]
      ), P(
        e,
        "padded",
        /*padded*/
        l[5]
      ), P(
        e,
        "highlight",
        /*highlight*/
        l[6]
      ), P(
        e,
        "transparent",
        /*transparent*/
        l[9]
      ), Me(e, "color", !/*disabled*/
      l[7] && /*_color*/
      l[12] ? (
        /*_color*/
        l[12]
      ) : "var(--block-label-text-color)"), Me(e, "--bg-color", /*disabled*/
      l[7] ? "auto" : (
        /*background*/
        l[10]
      )), Me(
        e,
        "margin-left",
        /*offset*/
        l[11] + "px"
      );
    },
    m(a, r) {
      hl(a, e, r), u && u.m(e, null), rt(e, t), rt(e, n), Nn(s, n, null), f = !0, i || (o = Bn(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), i = !0);
    },
    p(a, [r]) {
      /*show_label*/
      a[2] ? u ? u.p(a, r) : (u = Ht(a), u.c(), u.m(e, t)) : u && (u.d(1), u = null), (!f || r & /*size*/
      16) && P(
        n,
        "small",
        /*size*/
        a[4] === "small"
      ), (!f || r & /*size*/
      16) && P(
        n,
        "large",
        /*size*/
        a[4] === "large"
      ), (!f || r & /*size*/
      16) && P(
        n,
        "medium",
        /*size*/
        a[4] === "medium"
      ), (!f || r & /*disabled*/
      128) && (e.disabled = /*disabled*/
      a[7]), (!f || r & /*label*/
      2) && re(
        e,
        "aria-label",
        /*label*/
        a[1]
      ), (!f || r & /*hasPopup*/
      256) && re(
        e,
        "aria-haspopup",
        /*hasPopup*/
        a[8]
      ), (!f || r & /*label*/
      2) && re(
        e,
        "title",
        /*label*/
        a[1]
      ), (!f || r & /*pending*/
      8) && P(
        e,
        "pending",
        /*pending*/
        a[3]
      ), (!f || r & /*padded*/
      32) && P(
        e,
        "padded",
        /*padded*/
        a[5]
      ), (!f || r & /*highlight*/
      64) && P(
        e,
        "highlight",
        /*highlight*/
        a[6]
      ), (!f || r & /*transparent*/
      512) && P(
        e,
        "transparent",
        /*transparent*/
        a[9]
      ), r & /*disabled, _color*/
      4224 && Me(e, "color", !/*disabled*/
      a[7] && /*_color*/
      a[12] ? (
        /*_color*/
        a[12]
      ) : "var(--block-label-text-color)"), r & /*disabled, background*/
      1152 && Me(e, "--bg-color", /*disabled*/
      a[7] ? "auto" : (
        /*background*/
        a[10]
      )), r & /*offset*/
      2048 && Me(
        e,
        "margin-left",
        /*offset*/
        a[11] + "px"
      );
    },
    i(a) {
      f || (Pn(s.$$.fragment, a), f = !0);
    },
    o(a) {
      Yn(s.$$.fragment, a), f = !1;
    },
    d(a) {
      a && ml(e), u && u.d(), En(s), i = !1, o();
    }
  };
}
function On(l, e, t) {
  let n, { Icon: s } = e, { label: f = "" } = e, { show_label: i = !1 } = e, { pending: o = !1 } = e, { size: u = "small" } = e, { padded: a = !0 } = e, { highlight: r = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: c = !1 } = e, { color: h = "var(--block-label-text-color)" } = e, { transparent: L = !1 } = e, { background: M = "var(--background-fill-primary)" } = e, { offset: k = 0 } = e;
  function v(m) {
    Sn.call(this, l, m);
  }
  return l.$$set = (m) => {
    "Icon" in m && t(0, s = m.Icon), "label" in m && t(1, f = m.label), "show_label" in m && t(2, i = m.show_label), "pending" in m && t(3, o = m.pending), "size" in m && t(4, u = m.size), "padded" in m && t(5, a = m.padded), "highlight" in m && t(6, r = m.highlight), "disabled" in m && t(7, _ = m.disabled), "hasPopup" in m && t(8, c = m.hasPopup), "color" in m && t(13, h = m.color), "transparent" in m && t(9, L = m.transparent), "background" in m && t(10, M = m.background), "offset" in m && t(11, k = m.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = r ? "var(--color-accent)" : h);
  }, [
    s,
    f,
    i,
    o,
    u,
    a,
    r,
    _,
    c,
    L,
    M,
    k,
    n,
    h,
    v
  ];
}
class Un extends Zn {
  constructor(e) {
    super(), Tn(this, e, On, Kn, Dn, {
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
  SvelteComponent: Xn,
  append: it,
  attr: R,
  detach: Gn,
  init: Rn,
  insert: Wn,
  noop: st,
  safe_not_equal: Jn,
  set_style: fe,
  svg_element: Ie
} = window.__gradio__svelte__internal;
function Qn(l) {
  let e, t, n, s;
  return {
    c() {
      e = Ie("svg"), t = Ie("g"), n = Ie("path"), s = Ie("path"), R(n, "d", "M18,6L6.087,17.913"), fe(n, "fill", "none"), fe(n, "fill-rule", "nonzero"), fe(n, "stroke-width", "2px"), R(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), R(s, "d", "M4.364,4.364L19.636,19.636"), fe(s, "fill", "none"), fe(s, "fill-rule", "nonzero"), fe(s, "stroke-width", "2px"), R(e, "width", "100%"), R(e, "height", "100%"), R(e, "viewBox", "0 0 24 24"), R(e, "version", "1.1"), R(e, "xmlns", "http://www.w3.org/2000/svg"), R(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), R(e, "xml:space", "preserve"), R(e, "stroke", "currentColor"), fe(e, "fill-rule", "evenodd"), fe(e, "clip-rule", "evenodd"), fe(e, "stroke-linecap", "round"), fe(e, "stroke-linejoin", "round");
    },
    m(f, i) {
      Wn(f, e, i), it(e, t), it(t, n), it(e, s);
    },
    p: st,
    i: st,
    o: st,
    d(f) {
      f && Gn(e);
    }
  };
}
class xn extends Xn {
  constructor(e) {
    super(), Rn(this, e, null, Qn, Jn, {});
  }
}
const $n = [
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
], qt = {
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
$n.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: qt[e][t],
      secondary: qt[e][n]
    }
  }),
  {}
);
function Oe() {
}
function ei(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const bl = typeof window < "u";
let Ft = bl ? () => window.performance.now() : () => Date.now(), gl = bl ? (l) => requestAnimationFrame(l) : Oe;
const Se = /* @__PURE__ */ new Set();
function wl(l) {
  Se.forEach((e) => {
    e.c(l) || (Se.delete(e), e.f());
  }), Se.size !== 0 && gl(wl);
}
function ti(l) {
  let e;
  return Se.size === 0 && gl(wl), {
    promise: new Promise((t) => {
      Se.add(e = { c: l, f: t });
    }),
    abort() {
      Se.delete(e);
    }
  };
}
function li(l) {
  const e = l - 1;
  return e * e * e + 1;
}
const Ve = [];
function ni(l, e = Oe) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function s(o) {
    if (ei(l, o) && (l = o, t)) {
      const u = !Ve.length;
      for (const a of n)
        a[1](), Ve.push(a, l);
      if (u) {
        for (let a = 0; a < Ve.length; a += 2)
          Ve[a][0](Ve[a + 1]);
        Ve.length = 0;
      }
    }
  }
  function f(o) {
    s(o(l));
  }
  function i(o, u = Oe) {
    const a = [o, u];
    return n.add(a), n.size === 1 && (t = e(s, f) || Oe), o(l), () => {
      n.delete(a), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: s, update: f, subscribe: i };
}
function Zt(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function ct(l, e, t, n) {
  if (typeof t == "number" || Zt(t)) {
    const s = n - t, f = (t - e) / (l.dt || 1 / 60), i = l.opts.stiffness * s, o = l.opts.damping * f, u = (i - o) * l.inv_mass, a = (f + u) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(s) < l.opts.precision ? n : (l.settled = !1, Zt(t) ? new Date(t.getTime() + a) : t + a);
  } else {
    if (Array.isArray(t))
      return t.map(
        (s, f) => ct(l, e[f], t[f], n[f])
      );
    if (typeof t == "object") {
      const s = {};
      for (const f in t)
        s[f] = ct(l, e[f], t[f], n[f]);
      return s;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function St(l, e = {}) {
  const t = ni(l), { stiffness: n = 0.15, damping: s = 0.8, precision: f = 0.01 } = e;
  let i, o, u, a = l, r = l, _ = 1, c = 0, h = !1;
  function L(k, v = {}) {
    r = k;
    const m = u = {};
    return l == null || v.hard || M.stiffness >= 1 && M.damping >= 1 ? (h = !0, i = Ft(), a = k, t.set(l = r), Promise.resolve()) : (v.soft && (c = 1 / ((v.soft === !0 ? 0.5 : +v.soft) * 60), _ = 0), o || (i = Ft(), h = !1, o = ti((b) => {
      if (h)
        return h = !1, o = null, !1;
      _ = Math.min(_ + c, 1);
      const C = {
        inv_mass: _,
        opts: M,
        settled: !0,
        dt: (b - i) * 60 / 1e3
      }, T = ct(C, a, l, r);
      return i = b, a = l, t.set(l = T), C.settled && (o = null), !C.settled;
    })), new Promise((b) => {
      o.promise.then(() => {
        m === u && b();
      });
    }));
  }
  const M = {
    set: L,
    update: (k, v) => L(k(r, l), v),
    subscribe: t.subscribe,
    stiffness: n,
    damping: s,
    precision: f
  };
  return M;
}
function zt(l, { delay: e = 0, duration: t = 500, easing: n = li } = {}) {
  const s = parseFloat(getComputedStyle(l).height);
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (f) => {
      const i = f, o = `translateY(${(1 - f) * -10}px)`, u = f * s;
      return `
                opacity: ${i};
                transform: ${o};
                height: ${u}px;
            `;
    }
  };
}
const {
  SvelteComponent: ii,
  action_destroyer: bt,
  add_render_callback: si,
  append: F,
  attr: g,
  binding_callbacks: ft,
  bubble: He,
  check_outros: fi,
  create_bidirectional_transition: Et,
  create_component: oi,
  destroy_component: ai,
  destroy_each: vl,
  detach: $,
  element: B,
  ensure_array_like: Ue,
  group_outros: ui,
  init: ri,
  insert: ee,
  is_function: gt,
  listen: E,
  mount_component: _i,
  noop: Xe,
  run_all: wt,
  safe_not_equal: ci,
  set_data: vt,
  set_input_value: ze,
  space: te,
  svg_element: Ge,
  text: pt,
  toggle_class: Tt,
  transition_in: ot,
  transition_out: at
} = window.__gradio__svelte__internal, { beforeUpdate: di, afterUpdate: mi, createEventDispatcher: hi, tick: Bt } = window.__gradio__svelte__internal;
function Nt(l, e, t) {
  const n = l.slice();
  return n[47] = e[t], n;
}
function Dt(l, e, t) {
  const n = l.slice();
  return n[47] = e[t], n;
}
function bi(l) {
  let e;
  return {
    c() {
      e = pt(
        /*label*/
        l[3]
      );
    },
    m(t, n) {
      ee(t, e, n);
    },
    p(t, n) {
      n[0] & /*label*/
      8 && vt(
        e,
        /*label*/
        t[3]
      );
    },
    d(t) {
      t && $(e);
    }
  };
}
function gi(l) {
  let e, t, n, s, f, i;
  return {
    c() {
      e = B("textarea"), g(e, "data-testid", "textbox"), g(e, "class", "scroll-hide svelte-lsxp0u"), g(e, "dir", t = /*rtl*/
      l[10] ? "rtl" : "ltr"), g(
        e,
        "placeholder",
        /*placeholder*/
        l[2]
      ), g(
        e,
        "rows",
        /*lines*/
        l[1]
      ), e.disabled = /*disabled*/
      l[5], e.autofocus = /*autofocus*/
      l[11], g(e, "style", n = /*text_align*/
      l[12] ? "text-align: " + /*text_align*/
      l[12] : "");
    },
    m(o, u) {
      ee(o, e, u), ze(
        e,
        /*value*/
        l[0]
      ), l[38](e), /*autofocus*/
      l[11] && e.focus(), f || (i = [
        bt(s = /*text_area_resize*/
        l[21].call(
          null,
          e,
          /*value*/
          l[0]
        )),
        E(
          e,
          "input",
          /*textarea_input_handler_2*/
          l[37]
        ),
        E(
          e,
          "keypress",
          /*handle_keypress*/
          l[19]
        ),
        E(
          e,
          "blur",
          /*blur_handler_2*/
          l[29]
        ),
        E(
          e,
          "select",
          /*handle_select*/
          l[18]
        ),
        E(
          e,
          "focus",
          /*focus_handler_2*/
          l[30]
        ),
        E(
          e,
          "scroll",
          /*handle_scroll*/
          l[20]
        )
      ], f = !0);
    },
    p(o, u) {
      u[0] & /*rtl*/
      1024 && t !== (t = /*rtl*/
      o[10] ? "rtl" : "ltr") && g(e, "dir", t), u[0] & /*placeholder*/
      4 && g(
        e,
        "placeholder",
        /*placeholder*/
        o[2]
      ), u[0] & /*lines*/
      2 && g(
        e,
        "rows",
        /*lines*/
        o[1]
      ), u[0] & /*disabled*/
      32 && (e.disabled = /*disabled*/
      o[5]), u[0] & /*autofocus*/
      2048 && (e.autofocus = /*autofocus*/
      o[11]), u[0] & /*text_align*/
      4096 && n !== (n = /*text_align*/
      o[12] ? "text-align: " + /*text_align*/
      o[12] : "") && g(e, "style", n), s && gt(s.update) && u[0] & /*value*/
      1 && s.update.call(
        null,
        /*value*/
        o[0]
      ), u[0] & /*value*/
      1 && ze(
        e,
        /*value*/
        o[0]
      );
    },
    i: Xe,
    o: Xe,
    d(o) {
      o && $(e), l[38](null), f = !1, wt(i);
    }
  };
}
function wi(l) {
  let e, t, n, s, f, i, o, u, a;
  return {
    c() {
      e = B("div"), t = B("textarea"), i = te(), o = B("button"), o.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-lsxp0u"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#CCCCCC" class="svelte-lsxp0u"></path></svg>', g(t, "data-testid", "textbox"), g(t, "class", "scroll-hide svelte-lsxp0u"), g(t, "dir", n = /*rtl*/
      l[10] ? "rtl" : "ltr"), g(
        t,
        "placeholder",
        /*placeholder*/
        l[2]
      ), g(
        t,
        "rows",
        /*lines*/
        l[1]
      ), t.disabled = /*disabled*/
      l[5], t.autofocus = /*autofocus*/
      l[11], g(t, "style", s = /*text_align*/
      l[12] ? "text-align: " + /*text_align*/
      l[12] : ""), g(o, "class", "extend_button svelte-lsxp0u"), g(o, "aria-label", "Extend"), g(o, "aria-roledescription", "Extend text"), g(e, "class", "magic_container svelte-lsxp0u");
    },
    m(r, _) {
      ee(r, e, _), F(e, t), ze(
        t,
        /*value*/
        l[0]
      ), l[36](t), F(e, i), F(e, o), /*autofocus*/
      l[11] && t.focus(), u || (a = [
        bt(f = /*text_area_resize*/
        l[21].call(
          null,
          t,
          /*value*/
          l[0]
        )),
        E(
          t,
          "input",
          /*textarea_input_handler_1*/
          l[35]
        ),
        E(
          t,
          "keypress",
          /*handle_keypress*/
          l[19]
        ),
        E(
          t,
          "blur",
          /*blur_handler_1*/
          l[27]
        ),
        E(
          t,
          "select",
          /*handle_select*/
          l[18]
        ),
        E(
          t,
          "focus",
          /*focus_handler_1*/
          l[28]
        ),
        E(
          t,
          "scroll",
          /*handle_scroll*/
          l[20]
        ),
        E(
          o,
          "click",
          /*handle_extension*/
          l[16]
        )
      ], u = !0);
    },
    p(r, _) {
      _[0] & /*rtl*/
      1024 && n !== (n = /*rtl*/
      r[10] ? "rtl" : "ltr") && g(t, "dir", n), _[0] & /*placeholder*/
      4 && g(
        t,
        "placeholder",
        /*placeholder*/
        r[2]
      ), _[0] & /*lines*/
      2 && g(
        t,
        "rows",
        /*lines*/
        r[1]
      ), _[0] & /*disabled*/
      32 && (t.disabled = /*disabled*/
      r[5]), _[0] & /*autofocus*/
      2048 && (t.autofocus = /*autofocus*/
      r[11]), _[0] & /*text_align*/
      4096 && s !== (s = /*text_align*/
      r[12] ? "text-align: " + /*text_align*/
      r[12] : "") && g(t, "style", s), f && gt(f.update) && _[0] & /*value*/
      1 && f.update.call(
        null,
        /*value*/
        r[0]
      ), _[0] & /*value*/
      1 && ze(
        t,
        /*value*/
        r[0]
      );
    },
    i: Xe,
    o: Xe,
    d(r) {
      r && $(e), l[36](null), u = !1, wt(a);
    }
  };
}
function vi(l) {
  let e, t, n, s, f, i, o, u, a, r, _, c, h, L, M = (
    /*prompts*/
    l[8].length > 0 && It(l)
  ), k = (
    /*suffixes*/
    l[9].length > 0 && At(l)
  );
  return {
    c() {
      e = B("div"), t = B("textarea"), i = te(), o = B("button"), o.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-lsxp0u"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#ff6700" class="svelte-lsxp0u"></path></svg>', u = te(), a = B("div"), M && M.c(), r = te(), k && k.c(), g(t, "data-testid", "textbox"), g(t, "class", "scroll-hide svelte-lsxp0u"), g(t, "dir", n = /*rtl*/
      l[10] ? "rtl" : "ltr"), g(
        t,
        "placeholder",
        /*placeholder*/
        l[2]
      ), g(
        t,
        "rows",
        /*lines*/
        l[1]
      ), t.disabled = /*disabled*/
      l[5], t.autofocus = /*autofocus*/
      l[11], g(t, "style", s = /*text_align*/
      l[12] ? "text-align: " + /*text_align*/
      l[12] : ""), g(o, "class", "extend_button svelte-lsxp0u"), g(o, "aria-label", "Extend"), g(o, "aria-roledescription", "Extend text"), g(e, "class", "magic_container svelte-lsxp0u"), g(a, "class", "menu svelte-lsxp0u");
    },
    m(v, m) {
      ee(v, e, m), F(e, t), ze(
        t,
        /*value*/
        l[0]
      ), l[32](t), F(e, i), F(e, o), ee(v, u, m), ee(v, a, m), M && M.m(a, null), F(a, r), k && k.m(a, null), c = !0, /*autofocus*/
      l[11] && t.focus(), h || (L = [
        bt(f = /*text_area_resize*/
        l[21].call(
          null,
          t,
          /*value*/
          l[0]
        )),
        E(
          t,
          "input",
          /*textarea_input_handler*/
          l[31]
        ),
        E(
          t,
          "keypress",
          /*handle_keypress*/
          l[19]
        ),
        E(
          t,
          "blur",
          /*blur_handler*/
          l[25]
        ),
        E(
          t,
          "select",
          /*handle_select*/
          l[18]
        ),
        E(
          t,
          "focus",
          /*focus_handler*/
          l[26]
        ),
        E(
          t,
          "scroll",
          /*handle_scroll*/
          l[20]
        ),
        E(
          o,
          "click",
          /*handle_extension*/
          l[16]
        )
      ], h = !0);
    },
    p(v, m) {
      (!c || m[0] & /*rtl*/
      1024 && n !== (n = /*rtl*/
      v[10] ? "rtl" : "ltr")) && g(t, "dir", n), (!c || m[0] & /*placeholder*/
      4) && g(
        t,
        "placeholder",
        /*placeholder*/
        v[2]
      ), (!c || m[0] & /*lines*/
      2) && g(
        t,
        "rows",
        /*lines*/
        v[1]
      ), (!c || m[0] & /*disabled*/
      32) && (t.disabled = /*disabled*/
      v[5]), (!c || m[0] & /*autofocus*/
      2048) && (t.autofocus = /*autofocus*/
      v[11]), (!c || m[0] & /*text_align*/
      4096 && s !== (s = /*text_align*/
      v[12] ? "text-align: " + /*text_align*/
      v[12] : "")) && g(t, "style", s), f && gt(f.update) && m[0] & /*value*/
      1 && f.update.call(
        null,
        /*value*/
        v[0]
      ), m[0] & /*value*/
      1 && ze(
        t,
        /*value*/
        v[0]
      ), /*prompts*/
      v[8].length > 0 ? M ? M.p(v, m) : (M = It(v), M.c(), M.m(a, r)) : M && (M.d(1), M = null), /*suffixes*/
      v[9].length > 0 ? k ? k.p(v, m) : (k = At(v), k.c(), k.m(a, null)) : k && (k.d(1), k = null);
    },
    i(v) {
      c || (v && si(() => {
        c && (_ || (_ = Et(a, zt, {}, !0)), _.run(1));
      }), c = !0);
    },
    o(v) {
      v && (_ || (_ = Et(a, zt, {}, !1)), _.run(0)), c = !1;
    },
    d(v) {
      v && ($(e), $(u), $(a)), l[32](null), M && M.d(), k && k.d(), v && _ && _.end(), h = !1, wt(L);
    }
  };
}
function It(l) {
  let e, t, n, s, f = Ue(
    /*prompts*/
    l[8]
  ), i = [];
  for (let o = 0; o < f.length; o += 1)
    i[o] = jt(Dt(l, f, o));
  return {
    c() {
      e = B("div"), t = B("span"), t.textContent = "Best prompt structures", n = te(), s = B("ul");
      for (let o = 0; o < i.length; o += 1)
        i[o].c();
      g(s, "class", "svelte-lsxp0u"), g(e, "class", "menu_section svelte-lsxp0u");
    },
    m(o, u) {
      ee(o, e, u), F(e, t), F(e, n), F(e, s);
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(s, null);
    },
    p(o, u) {
      if (u[0] & /*addToTextbox, prompts*/
      131328) {
        f = Ue(
          /*prompts*/
          o[8]
        );
        let a;
        for (a = 0; a < f.length; a += 1) {
          const r = Dt(o, f, a);
          i[a] ? i[a].p(r, u) : (i[a] = jt(r), i[a].c(), i[a].m(s, null));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = f.length;
      }
    },
    d(o) {
      o && $(e), vl(i, o);
    }
  };
}
function jt(l) {
  let e, t, n = (
    /*word*/
    l[47] + ""
  ), s, f, i, o, u, a, r;
  function _() {
    return (
      /*click_handler*/
      l[33](
        /*word*/
        l[47]
      )
    );
  }
  return {
    c() {
      e = B("li"), t = B("button"), s = pt(n), f = te(), i = Ge("svg"), o = Ge("path"), u = te(), g(o, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), g(o, "fill", "#FF9A57"), g(o, "class", "svelte-lsxp0u"), g(i, "xmlns", "http://www.w3.org/2000/svg"), g(i, "width", "11"), g(i, "height", "12"), g(i, "viewBox", "0 0 11 12"), g(i, "fill", "none"), g(i, "class", "svelte-lsxp0u"), g(t, "class", "text_extension_button_prompt svelte-lsxp0u"), g(e, "class", "svelte-lsxp0u");
    },
    m(c, h) {
      ee(c, e, h), F(e, t), F(t, s), F(t, f), F(t, i), F(i, o), F(e, u), a || (r = E(t, "click", _), a = !0);
    },
    p(c, h) {
      l = c, h[0] & /*prompts*/
      256 && n !== (n = /*word*/
      l[47] + "") && vt(s, n);
    },
    d(c) {
      c && $(e), a = !1, r();
    }
  };
}
function At(l) {
  let e, t, n, s, f = Ue(
    /*suffixes*/
    l[9]
  ), i = [];
  for (let o = 0; o < f.length; o += 1)
    i[o] = Pt(Nt(l, f, o));
  return {
    c() {
      e = B("div"), t = B("span"), t.textContent = "Best style keywords", n = te(), s = B("ul");
      for (let o = 0; o < i.length; o += 1)
        i[o].c();
      g(s, "class", "svelte-lsxp0u"), g(e, "class", "menu_section svelte-lsxp0u");
    },
    m(o, u) {
      ee(o, e, u), F(e, t), F(e, n), F(e, s);
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(s, null);
    },
    p(o, u) {
      if (u[0] & /*addToTextbox, suffixes*/
      131584) {
        f = Ue(
          /*suffixes*/
          o[9]
        );
        let a;
        for (a = 0; a < f.length; a += 1) {
          const r = Nt(o, f, a);
          i[a] ? i[a].p(r, u) : (i[a] = Pt(r), i[a].c(), i[a].m(s, null));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = f.length;
      }
    },
    d(o) {
      o && $(e), vl(i, o);
    }
  };
}
function Pt(l) {
  let e, t, n = (
    /*word*/
    l[47] + ""
  ), s, f, i, o, u, a, r;
  function _() {
    return (
      /*click_handler_1*/
      l[34](
        /*word*/
        l[47]
      )
    );
  }
  return {
    c() {
      e = B("li"), t = B("button"), s = pt(n), f = te(), i = Ge("svg"), o = Ge("path"), u = te(), g(o, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), g(o, "fill", "#FF9A57"), g(o, "class", "svelte-lsxp0u"), g(i, "xmlns", "http://www.w3.org/2000/svg"), g(i, "width", "11"), g(i, "height", "12"), g(i, "viewBox", "0 0 11 12"), g(i, "fill", "none"), g(i, "class", "svelte-lsxp0u"), g(t, "class", "text_extension_button svelte-lsxp0u"), g(e, "class", "svelte-lsxp0u");
    },
    m(c, h) {
      ee(c, e, h), F(e, t), F(t, s), F(t, f), F(t, i), F(i, o), F(e, u), a || (r = E(t, "click", _), a = !0);
    },
    p(c, h) {
      l = c, h[0] & /*suffixes*/
      512 && n !== (n = /*word*/
      l[47] + "") && vt(s, n);
    },
    d(c) {
      c && $(e), a = !1, r();
    }
  };
}
function pi(l) {
  let e, t, n, s, f, i, o;
  t = new Fn({
    props: {
      show_label: (
        /*show_label*/
        l[6]
      ),
      info: (
        /*info*/
        l[4]
      ),
      $$slots: { default: [bi] },
      $$scope: { ctx: l }
    }
  });
  const u = [vi, wi, gi], a = [];
  function r(_, c) {
    return (
      /*show_menu*/
      _[14] && /*show_magic*/
      _[15] ? 0 : !/*show_menu*/
      _[14] && /*show_magic*/
      _[15] ? 1 : 2
    );
  }
  return f = r(l), i = a[f] = u[f](l), {
    c() {
      e = B("label"), oi(t.$$.fragment), n = te(), s = B("div"), i.c(), g(s, "class", "input-container"), g(e, "class", "svelte-lsxp0u"), Tt(
        e,
        "container",
        /*container*/
        l[7]
      );
    },
    m(_, c) {
      ee(_, e, c), _i(t, e, null), F(e, n), F(e, s), a[f].m(s, null), o = !0;
    },
    p(_, c) {
      const h = {};
      c[0] & /*show_label*/
      64 && (h.show_label = /*show_label*/
      _[6]), c[0] & /*info*/
      16 && (h.info = /*info*/
      _[4]), c[0] & /*label*/
      8 | c[1] & /*$$scope*/
      2097152 && (h.$$scope = { dirty: c, ctx: _ }), t.$set(h);
      let L = f;
      f = r(_), f === L ? a[f].p(_, c) : (ui(), at(a[L], 1, 1, () => {
        a[L] = null;
      }), fi(), i = a[f], i ? i.p(_, c) : (i = a[f] = u[f](_), i.c()), ot(i, 1), i.m(s, null)), (!o || c[0] & /*container*/
      128) && Tt(
        e,
        "container",
        /*container*/
        _[7]
      );
    },
    i(_) {
      o || (ot(t.$$.fragment, _), ot(i), o = !0);
    },
    o(_) {
      at(t.$$.fragment, _), at(i), o = !1;
    },
    d(_) {
      _ && $(e), ai(t), a[f].d();
    }
  };
}
function ki(l, e, t) {
  var n = this && this.__awaiter || function(d, S, D, A) {
    function me(Te) {
      return Te instanceof D ? Te : new D(function(De) {
        De(Te);
      });
    }
    return new (D || (D = Promise))(function(Te, De) {
      function ql(he) {
        try {
          lt(A.next(he));
        } catch (nt) {
          De(nt);
        }
      }
      function Fl(he) {
        try {
          lt(A.throw(he));
        } catch (nt) {
          De(nt);
        }
      }
      function lt(he) {
        he.done ? Te(he.value) : me(he.value).then(ql, Fl);
      }
      lt((A = A.apply(d, S || [])).next());
    });
  };
  let { value: s = "" } = e, { value_is_output: f = !1 } = e, { lines: i = 1 } = e, { placeholder: o = "Type here..." } = e, { label: u } = e, { info: a = void 0 } = e, { disabled: r = !1 } = e, { show_label: _ = !0 } = e, { container: c = !0 } = e, { max_lines: h } = e, { prompts: L = [] } = e, { suffixes: M = [] } = e, { rtl: k = !1 } = e, { autofocus: v = !1 } = e, { text_align: m = void 0 } = e, { autoscroll: b = !0 } = e, C, T = !1, p, N = 0, I = !1, le = L.length > 0 || M.length > 0;
  const j = hi();
  di(() => {
    p = C && C.offsetHeight + C.scrollTop > C.scrollHeight - 100;
  });
  const ne = () => {
    p && b && !I && C.scrollTo(0, C.scrollHeight);
  };
  function ie() {
    j("change", s), f || j("input");
  }
  mi(() => {
    v && C.focus(), p && b && ne(), t(22, f = !1), t(15, le = L.length > 0 || M.length > 0);
  });
  function ge() {
    return n(this, void 0, void 0, function* () {
      t(14, T = !T);
    });
  }
  function Y(d) {
    t(0, s += `${d} `);
  }
  function ue(d) {
    const S = d.target, D = S.value, A = [S.selectionStart, S.selectionEnd];
    j("select", { value: D.substring(...A), index: A });
  }
  function O(d) {
    return n(this, void 0, void 0, function* () {
      yield Bt(), (d.key === "Enter" && d.shiftKey && i > 1 || d.key === "Enter" && !d.shiftKey && i === 1 && h >= 1) && (d.preventDefault(), j("submit"));
    });
  }
  function we(d) {
    const S = d.target, D = S.scrollTop;
    D < N && (I = !0), N = D;
    const A = S.scrollHeight - S.clientHeight;
    D >= A && (I = !1);
  }
  function _e(d) {
    return n(this, void 0, void 0, function* () {
      if (yield Bt(), i === h)
        return;
      let S = h === void 0 ? !1 : h === void 0 ? 21 * 11 : 21 * (h + 1), D = 21 * (i + 1);
      const A = d.target;
      A.style.height = "1px";
      let me;
      S && A.scrollHeight > S ? me = S : A.scrollHeight < D ? me = D : me = A.scrollHeight, A.style.height = `${me}px`;
    });
  }
  function ve(d, S) {
    if (i !== h && (d.style.overflowY = "scroll", d.addEventListener("input", _e), !!S.trim()))
      return _e({ target: d }), {
        destroy: () => d.removeEventListener("input", _e)
      };
  }
  function w(d) {
    He.call(this, l, d);
  }
  function pe(d) {
    He.call(this, l, d);
  }
  function We(d) {
    He.call(this, l, d);
  }
  function Je(d) {
    He.call(this, l, d);
  }
  function Qe(d) {
    He.call(this, l, d);
  }
  function y(d) {
    He.call(this, l, d);
  }
  function xe() {
    s = this.value, t(0, s);
  }
  function ke(d) {
    ft[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  const Ce = (d) => Y(d), $e = (d) => Y(d);
  function de() {
    s = this.value, t(0, s);
  }
  function ye(d) {
    ft[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  function et() {
    s = this.value, t(0, s);
  }
  function tt(d) {
    ft[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  return l.$$set = (d) => {
    "value" in d && t(0, s = d.value), "value_is_output" in d && t(22, f = d.value_is_output), "lines" in d && t(1, i = d.lines), "placeholder" in d && t(2, o = d.placeholder), "label" in d && t(3, u = d.label), "info" in d && t(4, a = d.info), "disabled" in d && t(5, r = d.disabled), "show_label" in d && t(6, _ = d.show_label), "container" in d && t(7, c = d.container), "max_lines" in d && t(23, h = d.max_lines), "prompts" in d && t(8, L = d.prompts), "suffixes" in d && t(9, M = d.suffixes), "rtl" in d && t(10, k = d.rtl), "autofocus" in d && t(11, v = d.autofocus), "text_align" in d && t(12, m = d.text_align), "autoscroll" in d && t(24, b = d.autoscroll);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*value*/
    1 && s === null && t(0, s = ""), l.$$.dirty[0] & /*value, el, lines, max_lines*/
    8396803 && C && i !== h && _e({ target: C }), l.$$.dirty[0] & /*value*/
    1 && ie();
  }, [
    s,
    i,
    o,
    u,
    a,
    r,
    _,
    c,
    L,
    M,
    k,
    v,
    m,
    C,
    T,
    le,
    ge,
    Y,
    ue,
    O,
    we,
    ve,
    f,
    h,
    b,
    w,
    pe,
    We,
    Je,
    Qe,
    y,
    xe,
    ke,
    Ce,
    $e,
    de,
    ye,
    et,
    tt
  ];
}
class Ci extends ii {
  constructor(e) {
    super(), ri(
      this,
      e,
      ki,
      pi,
      ci,
      {
        value: 0,
        value_is_output: 22,
        lines: 1,
        placeholder: 2,
        label: 3,
        info: 4,
        disabled: 5,
        show_label: 6,
        container: 7,
        max_lines: 23,
        prompts: 8,
        suffixes: 9,
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
function Fe(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
const {
  SvelteComponent: yi,
  append: W,
  attr: q,
  component_subscribe: Yt,
  detach: Li,
  element: Mi,
  init: Vi,
  insert: Hi,
  noop: Kt,
  safe_not_equal: qi,
  set_style: je,
  svg_element: J,
  toggle_class: Ot
} = window.__gradio__svelte__internal, { onMount: Fi } = window.__gradio__svelte__internal;
function Zi(l) {
  let e, t, n, s, f, i, o, u, a, r, _, c;
  return {
    c() {
      e = Mi("div"), t = J("svg"), n = J("g"), s = J("path"), f = J("path"), i = J("path"), o = J("path"), u = J("g"), a = J("path"), r = J("path"), _ = J("path"), c = J("path"), q(s, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(s, "fill", "#FF7C00"), q(s, "fill-opacity", "0.4"), q(s, "class", "svelte-43sxxs"), q(f, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(f, "fill", "#FF7C00"), q(f, "class", "svelte-43sxxs"), q(i, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(o, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(o, "fill", "#FF7C00"), q(o, "class", "svelte-43sxxs"), je(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(a, "fill", "#FF7C00"), q(a, "fill-opacity", "0.4"), q(a, "class", "svelte-43sxxs"), q(r, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(r, "fill", "#FF7C00"), q(r, "class", "svelte-43sxxs"), q(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(_, "fill", "#FF7C00"), q(_, "fill-opacity", "0.4"), q(_, "class", "svelte-43sxxs"), q(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), je(u, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Ot(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(h, L) {
      Hi(h, e, L), W(e, t), W(t, n), W(n, s), W(n, f), W(n, i), W(n, o), W(t, u), W(u, a), W(u, r), W(u, _), W(u, c);
    },
    p(h, [L]) {
      L & /*$top*/
      2 && je(n, "transform", "translate(" + /*$top*/
      h[1][0] + "px, " + /*$top*/
      h[1][1] + "px)"), L & /*$bottom*/
      4 && je(u, "transform", "translate(" + /*$bottom*/
      h[2][0] + "px, " + /*$bottom*/
      h[2][1] + "px)"), L & /*margin*/
      1 && Ot(
        e,
        "margin",
        /*margin*/
        h[0]
      );
    },
    i: Kt,
    o: Kt,
    d(h) {
      h && Li(e);
    }
  };
}
function Si(l, e, t) {
  let n, s;
  var f = this && this.__awaiter || function(h, L, M, k) {
    function v(m) {
      return m instanceof M ? m : new M(function(b) {
        b(m);
      });
    }
    return new (M || (M = Promise))(function(m, b) {
      function C(N) {
        try {
          p(k.next(N));
        } catch (I) {
          b(I);
        }
      }
      function T(N) {
        try {
          p(k.throw(N));
        } catch (I) {
          b(I);
        }
      }
      function p(N) {
        N.done ? m(N.value) : v(N.value).then(C, T);
      }
      p((k = k.apply(h, L || [])).next());
    });
  };
  let { margin: i = !0 } = e;
  const o = St([0, 0]);
  Yt(l, o, (h) => t(1, n = h));
  const u = St([0, 0]);
  Yt(l, u, (h) => t(2, s = h));
  let a;
  function r() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([o.set([125, 140]), u.set([-125, -140])]), yield Promise.all([o.set([-125, 140]), u.set([125, -140])]), yield Promise.all([o.set([-125, 0]), u.set([125, -0])]), yield Promise.all([o.set([125, 0]), u.set([-125, 0])]);
    });
  }
  function _() {
    return f(this, void 0, void 0, function* () {
      yield r(), a || _();
    });
  }
  function c() {
    return f(this, void 0, void 0, function* () {
      yield Promise.all([o.set([125, 0]), u.set([-125, 0])]), _();
    });
  }
  return Fi(() => (c(), () => a = !0)), l.$$set = (h) => {
    "margin" in h && t(0, i = h.margin);
  }, [i, n, s, o, u];
}
class zi extends yi {
  constructor(e) {
    super(), Vi(this, e, Si, Zi, qi, { margin: 0 });
  }
}
const {
  SvelteComponent: Ei,
  append: be,
  attr: x,
  binding_callbacks: Ut,
  check_outros: dt,
  create_component: pl,
  create_slot: kl,
  destroy_component: Cl,
  destroy_each: yl,
  detach: V,
  element: oe,
  empty: Ee,
  ensure_array_like: Re,
  get_all_dirty_from_scope: Ll,
  get_slot_changes: Ml,
  group_outros: mt,
  init: Ti,
  insert: H,
  mount_component: Vl,
  noop: ht,
  safe_not_equal: Bi,
  set_data: G,
  set_style: ce,
  space: X,
  text: z,
  toggle_class: U,
  transition_in: Q,
  transition_out: ae,
  update_slot_base: Hl
} = window.__gradio__svelte__internal, { tick: Ni } = window.__gradio__svelte__internal, { onDestroy: Di } = window.__gradio__svelte__internal, { createEventDispatcher: Ii } = window.__gradio__svelte__internal, ji = (l) => ({}), Xt = (l) => ({}), Ai = (l) => ({}), Gt = (l) => ({});
function Rt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function Wt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function Pi(l) {
  let e, t, n, s, f = (
    /*i18n*/
    l[1]("common.error") + ""
  ), i, o, u;
  t = new Un({
    props: {
      Icon: xn,
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
  ), r = kl(
    a,
    l,
    /*$$scope*/
    l[29],
    Xt
  );
  return {
    c() {
      e = oe("div"), pl(t.$$.fragment), n = X(), s = oe("span"), i = z(f), o = X(), r && r.c(), x(e, "class", "clear-status svelte-vopvsi"), x(s, "class", "error svelte-vopvsi");
    },
    m(_, c) {
      H(_, e, c), Vl(t, e, null), H(_, n, c), H(_, s, c), be(s, i), H(_, o, c), r && r.m(_, c), u = !0;
    },
    p(_, c) {
      const h = {};
      c[0] & /*i18n*/
      2 && (h.label = /*i18n*/
      _[1]("common.clear")), t.$set(h), (!u || c[0] & /*i18n*/
      2) && f !== (f = /*i18n*/
      _[1]("common.error") + "") && G(i, f), r && r.p && (!u || c[0] & /*$$scope*/
      536870912) && Hl(
        r,
        a,
        _,
        /*$$scope*/
        _[29],
        u ? Ml(
          a,
          /*$$scope*/
          _[29],
          c,
          ji
        ) : Ll(
          /*$$scope*/
          _[29]
        ),
        Xt
      );
    },
    i(_) {
      u || (Q(t.$$.fragment, _), Q(r, _), u = !0);
    },
    o(_) {
      ae(t.$$.fragment, _), ae(r, _), u = !1;
    },
    d(_) {
      _ && (V(e), V(n), V(s), V(o)), Cl(t), r && r.d(_);
    }
  };
}
function Yi(l) {
  let e, t, n, s, f, i, o, u, a, r = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Jt(l)
  );
  function _(b, C) {
    if (
      /*progress*/
      b[7]
    )
      return Ui;
    if (
      /*queue_position*/
      b[2] !== null && /*queue_size*/
      b[3] !== void 0 && /*queue_position*/
      b[2] >= 0
    )
      return Oi;
    if (
      /*queue_position*/
      b[2] === 0
    )
      return Ki;
  }
  let c = _(l), h = c && c(l), L = (
    /*timer*/
    l[5] && $t(l)
  );
  const M = [Wi, Ri], k = [];
  function v(b, C) {
    return (
      /*last_progress_level*/
      b[15] != null ? 0 : (
        /*show_progress*/
        b[6] === "full" ? 1 : -1
      )
    );
  }
  ~(f = v(l)) && (i = k[f] = M[f](l));
  let m = !/*timer*/
  l[5] && fl(l);
  return {
    c() {
      r && r.c(), e = X(), t = oe("div"), h && h.c(), n = X(), L && L.c(), s = X(), i && i.c(), o = X(), m && m.c(), u = Ee(), x(t, "class", "progress-text svelte-vopvsi"), U(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), U(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(b, C) {
      r && r.m(b, C), H(b, e, C), H(b, t, C), h && h.m(t, null), be(t, n), L && L.m(t, null), H(b, s, C), ~f && k[f].m(b, C), H(b, o, C), m && m.m(b, C), H(b, u, C), a = !0;
    },
    p(b, C) {
      /*variant*/
      b[8] === "default" && /*show_eta_bar*/
      b[18] && /*show_progress*/
      b[6] === "full" ? r ? r.p(b, C) : (r = Jt(b), r.c(), r.m(e.parentNode, e)) : r && (r.d(1), r = null), c === (c = _(b)) && h ? h.p(b, C) : (h && h.d(1), h = c && c(b), h && (h.c(), h.m(t, n))), /*timer*/
      b[5] ? L ? L.p(b, C) : (L = $t(b), L.c(), L.m(t, null)) : L && (L.d(1), L = null), (!a || C[0] & /*variant*/
      256) && U(
        t,
        "meta-text-center",
        /*variant*/
        b[8] === "center"
      ), (!a || C[0] & /*variant*/
      256) && U(
        t,
        "meta-text",
        /*variant*/
        b[8] === "default"
      );
      let T = f;
      f = v(b), f === T ? ~f && k[f].p(b, C) : (i && (mt(), ae(k[T], 1, 1, () => {
        k[T] = null;
      }), dt()), ~f ? (i = k[f], i ? i.p(b, C) : (i = k[f] = M[f](b), i.c()), Q(i, 1), i.m(o.parentNode, o)) : i = null), /*timer*/
      b[5] ? m && (mt(), ae(m, 1, 1, () => {
        m = null;
      }), dt()) : m ? (m.p(b, C), C[0] & /*timer*/
      32 && Q(m, 1)) : (m = fl(b), m.c(), Q(m, 1), m.m(u.parentNode, u));
    },
    i(b) {
      a || (Q(i), Q(m), a = !0);
    },
    o(b) {
      ae(i), ae(m), a = !1;
    },
    d(b) {
      b && (V(e), V(t), V(s), V(o), V(u)), r && r.d(b), h && h.d(), L && L.d(), ~f && k[f].d(b), m && m.d(b);
    }
  };
}
function Jt(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = oe("div"), x(e, "class", "eta-bar svelte-vopvsi"), ce(e, "transform", t);
    },
    m(n, s) {
      H(n, e, s);
    },
    p(n, s) {
      s[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && ce(e, "transform", t);
    },
    d(n) {
      n && V(e);
    }
  };
}
function Ki(l) {
  let e;
  return {
    c() {
      e = z("processing |");
    },
    m(t, n) {
      H(t, e, n);
    },
    p: ht,
    d(t) {
      t && V(e);
    }
  };
}
function Oi(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, s, f, i;
  return {
    c() {
      e = z("queue: "), n = z(t), s = z("/"), f = z(
        /*queue_size*/
        l[3]
      ), i = z(" |");
    },
    m(o, u) {
      H(o, e, u), H(o, n, u), H(o, s, u), H(o, f, u), H(o, i, u);
    },
    p(o, u) {
      u[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      o[2] + 1 + "") && G(n, t), u[0] & /*queue_size*/
      8 && G(
        f,
        /*queue_size*/
        o[3]
      );
    },
    d(o) {
      o && (V(e), V(n), V(s), V(f), V(i));
    }
  };
}
function Ui(l) {
  let e, t = Re(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = xt(Wt(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Ee();
    },
    m(s, f) {
      for (let i = 0; i < n.length; i += 1)
        n[i] && n[i].m(s, f);
      H(s, e, f);
    },
    p(s, f) {
      if (f[0] & /*progress*/
      128) {
        t = Re(
          /*progress*/
          s[7]
        );
        let i;
        for (i = 0; i < t.length; i += 1) {
          const o = Wt(s, t, i);
          n[i] ? n[i].p(o, f) : (n[i] = xt(o), n[i].c(), n[i].m(e.parentNode, e));
        }
        for (; i < n.length; i += 1)
          n[i].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && V(e), yl(n, s);
    }
  };
}
function Qt(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, s, f = " ", i;
  function o(r, _) {
    return (
      /*p*/
      r[41].length != null ? Gi : Xi
    );
  }
  let u = o(l), a = u(l);
  return {
    c() {
      a.c(), e = X(), n = z(t), s = z(" | "), i = z(f);
    },
    m(r, _) {
      a.m(r, _), H(r, e, _), H(r, n, _), H(r, s, _), H(r, i, _);
    },
    p(r, _) {
      u === (u = o(r)) && a ? a.p(r, _) : (a.d(1), a = u(r), a && (a.c(), a.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      r[41].unit + "") && G(n, t);
    },
    d(r) {
      r && (V(e), V(n), V(s), V(i)), a.d(r);
    }
  };
}
function Xi(l) {
  let e = Fe(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      H(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = Fe(
        /*p*/
        n[41].index || 0
      ) + "") && G(t, e);
    },
    d(n) {
      n && V(t);
    }
  };
}
function Gi(l) {
  let e = Fe(
    /*p*/
    l[41].index || 0
  ) + "", t, n, s = Fe(
    /*p*/
    l[41].length
  ) + "", f;
  return {
    c() {
      t = z(e), n = z("/"), f = z(s);
    },
    m(i, o) {
      H(i, t, o), H(i, n, o), H(i, f, o);
    },
    p(i, o) {
      o[0] & /*progress*/
      128 && e !== (e = Fe(
        /*p*/
        i[41].index || 0
      ) + "") && G(t, e), o[0] & /*progress*/
      128 && s !== (s = Fe(
        /*p*/
        i[41].length
      ) + "") && G(f, s);
    },
    d(i) {
      i && (V(t), V(n), V(f));
    }
  };
}
function xt(l) {
  let e, t = (
    /*p*/
    l[41].index != null && Qt(l)
  );
  return {
    c() {
      t && t.c(), e = Ee();
    },
    m(n, s) {
      t && t.m(n, s), H(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].index != null ? t ? t.p(n, s) : (t = Qt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && V(e), t && t.d(n);
    }
  };
}
function $t(l) {
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
    m(f, i) {
      H(f, e, i), H(f, n, i), H(f, s, i);
    },
    p(f, i) {
      i[0] & /*formatted_timer*/
      1048576 && G(
        e,
        /*formatted_timer*/
        f[20]
      ), i[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      f[0] ? `/${/*formatted_eta*/
      f[19]}` : "") && G(n, t);
    },
    d(f) {
      f && (V(e), V(n), V(s));
    }
  };
}
function Ri(l) {
  let e, t;
  return e = new zi({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      pl(e.$$.fragment);
    },
    m(n, s) {
      Vl(e, n, s), t = !0;
    },
    p(n, s) {
      const f = {};
      s[0] & /*variant*/
      256 && (f.margin = /*variant*/
      n[8] === "default"), e.$set(f);
    },
    i(n) {
      t || (Q(e.$$.fragment, n), t = !0);
    },
    o(n) {
      ae(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Cl(e, n);
    }
  };
}
function Wi(l) {
  let e, t, n, s, f, i = `${/*last_progress_level*/
  l[15] * 100}%`, o = (
    /*progress*/
    l[7] != null && el(l)
  );
  return {
    c() {
      e = oe("div"), t = oe("div"), o && o.c(), n = X(), s = oe("div"), f = oe("div"), x(t, "class", "progress-level-inner svelte-vopvsi"), x(f, "class", "progress-bar svelte-vopvsi"), ce(f, "width", i), x(s, "class", "progress-bar-wrap svelte-vopvsi"), x(e, "class", "progress-level svelte-vopvsi");
    },
    m(u, a) {
      H(u, e, a), be(e, t), o && o.m(t, null), be(e, n), be(e, s), be(s, f), l[31](f);
    },
    p(u, a) {
      /*progress*/
      u[7] != null ? o ? o.p(u, a) : (o = el(u), o.c(), o.m(t, null)) : o && (o.d(1), o = null), a[0] & /*last_progress_level*/
      32768 && i !== (i = `${/*last_progress_level*/
      u[15] * 100}%`) && ce(f, "width", i);
    },
    i: ht,
    o: ht,
    d(u) {
      u && V(e), o && o.d(), l[31](null);
    }
  };
}
function el(l) {
  let e, t = Re(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = sl(Rt(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Ee();
    },
    m(s, f) {
      for (let i = 0; i < n.length; i += 1)
        n[i] && n[i].m(s, f);
      H(s, e, f);
    },
    p(s, f) {
      if (f[0] & /*progress_level, progress*/
      16512) {
        t = Re(
          /*progress*/
          s[7]
        );
        let i;
        for (i = 0; i < t.length; i += 1) {
          const o = Rt(s, t, i);
          n[i] ? n[i].p(o, f) : (n[i] = sl(o), n[i].c(), n[i].m(e.parentNode, e));
        }
        for (; i < n.length; i += 1)
          n[i].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && V(e), yl(n, s);
    }
  };
}
function tl(l) {
  let e, t, n, s, f = (
    /*i*/
    l[43] !== 0 && Ji()
  ), i = (
    /*p*/
    l[41].desc != null && ll(l)
  ), o = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && nl()
  ), u = (
    /*progress_level*/
    l[14] != null && il(l)
  );
  return {
    c() {
      f && f.c(), e = X(), i && i.c(), t = X(), o && o.c(), n = X(), u && u.c(), s = Ee();
    },
    m(a, r) {
      f && f.m(a, r), H(a, e, r), i && i.m(a, r), H(a, t, r), o && o.m(a, r), H(a, n, r), u && u.m(a, r), H(a, s, r);
    },
    p(a, r) {
      /*p*/
      a[41].desc != null ? i ? i.p(a, r) : (i = ll(a), i.c(), i.m(t.parentNode, t)) : i && (i.d(1), i = null), /*p*/
      a[41].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[43]
      ] != null ? o || (o = nl(), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null), /*progress_level*/
      a[14] != null ? u ? u.p(a, r) : (u = il(a), u.c(), u.m(s.parentNode, s)) : u && (u.d(1), u = null);
    },
    d(a) {
      a && (V(e), V(t), V(n), V(s)), f && f.d(a), i && i.d(a), o && o.d(a), u && u.d(a);
    }
  };
}
function Ji(l) {
  let e;
  return {
    c() {
      e = z(" /");
    },
    m(t, n) {
      H(t, e, n);
    },
    d(t) {
      t && V(e);
    }
  };
}
function ll(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      H(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && G(t, e);
    },
    d(n) {
      n && V(t);
    }
  };
}
function nl(l) {
  let e;
  return {
    c() {
      e = z("-");
    },
    m(t, n) {
      H(t, e, n);
    },
    d(t) {
      t && V(e);
    }
  };
}
function il(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = z(e), n = z("%");
    },
    m(s, f) {
      H(s, t, f), H(s, n, f);
    },
    p(s, f) {
      f[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (s[14][
        /*i*/
        s[43]
      ] || 0)).toFixed(1) + "") && G(t, e);
    },
    d(s) {
      s && (V(t), V(n));
    }
  };
}
function sl(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && tl(l)
  );
  return {
    c() {
      t && t.c(), e = Ee();
    },
    m(n, s) {
      t && t.m(n, s), H(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, s) : (t = tl(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && V(e), t && t.d(n);
    }
  };
}
function fl(l) {
  let e, t, n, s;
  const f = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), i = kl(
    f,
    l,
    /*$$scope*/
    l[29],
    Gt
  );
  return {
    c() {
      e = oe("p"), t = z(
        /*loading_text*/
        l[9]
      ), n = X(), i && i.c(), x(e, "class", "loading svelte-vopvsi");
    },
    m(o, u) {
      H(o, e, u), be(e, t), H(o, n, u), i && i.m(o, u), s = !0;
    },
    p(o, u) {
      (!s || u[0] & /*loading_text*/
      512) && G(
        t,
        /*loading_text*/
        o[9]
      ), i && i.p && (!s || u[0] & /*$$scope*/
      536870912) && Hl(
        i,
        f,
        o,
        /*$$scope*/
        o[29],
        s ? Ml(
          f,
          /*$$scope*/
          o[29],
          u,
          Ai
        ) : Ll(
          /*$$scope*/
          o[29]
        ),
        Gt
      );
    },
    i(o) {
      s || (Q(i, o), s = !0);
    },
    o(o) {
      ae(i, o), s = !1;
    },
    d(o) {
      o && (V(e), V(n)), i && i.d(o);
    }
  };
}
function Qi(l) {
  let e, t, n, s, f;
  const i = [Yi, Pi], o = [];
  function u(a, r) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = u(l)) && (n = o[t] = i[t](l)), {
    c() {
      e = oe("div"), n && n.c(), x(e, "class", s = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-vopvsi"), U(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), U(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), U(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), U(
        e,
        "border",
        /*border*/
        l[12]
      ), ce(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), ce(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(a, r) {
      H(a, e, r), ~t && o[t].m(e, null), l[33](e), f = !0;
    },
    p(a, r) {
      let _ = t;
      t = u(a), t === _ ? ~t && o[t].p(a, r) : (n && (mt(), ae(o[_], 1, 1, () => {
        o[_] = null;
      }), dt()), ~t ? (n = o[t], n ? n.p(a, r) : (n = o[t] = i[t](a), n.c()), Q(n, 1), n.m(e, null)) : n = null), (!f || r[0] & /*variant, show_progress*/
      320 && s !== (s = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-vopvsi")) && x(e, "class", s), (!f || r[0] & /*variant, show_progress, status, show_progress*/
      336) && U(e, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!f || r[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && U(
        e,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!f || r[0] & /*variant, show_progress, status*/
      336) && U(
        e,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!f || r[0] & /*variant, show_progress, border*/
      4416) && U(
        e,
        "border",
        /*border*/
        a[12]
      ), r[0] & /*absolute*/
      1024 && ce(
        e,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), r[0] & /*absolute*/
      1024 && ce(
        e,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      f || (Q(n), f = !0);
    },
    o(a) {
      ae(n), f = !1;
    },
    d(a) {
      a && V(e), ~t && o[t].d(), l[33](null);
    }
  };
}
var xi = function(l, e, t, n) {
  function s(f) {
    return f instanceof t ? f : new t(function(i) {
      i(f);
    });
  }
  return new (t || (t = Promise))(function(f, i) {
    function o(r) {
      try {
        a(n.next(r));
      } catch (_) {
        i(_);
      }
    }
    function u(r) {
      try {
        a(n.throw(r));
      } catch (_) {
        i(_);
      }
    }
    function a(r) {
      r.done ? f(r.value) : s(r.value).then(o, u);
    }
    a((n = n.apply(l, e || [])).next());
  });
};
let Ae = [], ut = !1;
function $i(l) {
  return xi(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Ae.push(e), !ut)
        ut = !0;
      else
        return;
      yield Ni(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let s = 0; s < Ae.length; s++) {
          const i = Ae[s].getBoundingClientRect();
          (s === 0 || i.top + window.scrollY <= n[0]) && (n[0] = i.top + window.scrollY, n[1] = s);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), ut = !1, Ae = [];
      });
    }
  });
}
function es(l, e, t) {
  let n, { $$slots: s = {}, $$scope: f } = e;
  this && this.__awaiter;
  const i = Ii();
  let { i18n: o } = e, { eta: u = null } = e, { queue_position: a } = e, { queue_size: r } = e, { status: _ } = e, { scroll_to_output: c = !1 } = e, { timer: h = !0 } = e, { show_progress: L = "full" } = e, { message: M = null } = e, { progress: k = null } = e, { variant: v = "default" } = e, { loading_text: m = "Loading..." } = e, { absolute: b = !0 } = e, { translucent: C = !1 } = e, { border: T = !1 } = e, { autoscroll: p } = e, N, I = !1, le = 0, j = 0, ne = null, ie = null, ge = 0, Y = null, ue, O = null, we = !0;
  const _e = () => {
    t(0, u = t(27, ne = t(19, pe = null))), t(25, le = performance.now()), t(26, j = 0), I = !0, ve();
  };
  function ve() {
    requestAnimationFrame(() => {
      t(26, j = (performance.now() - le) / 1e3), I && ve();
    });
  }
  function w() {
    t(26, j = 0), t(0, u = t(27, ne = t(19, pe = null))), I && (I = !1);
  }
  Di(() => {
    I && w();
  });
  let pe = null;
  function We(y) {
    Ut[y ? "unshift" : "push"](() => {
      O = y, t(16, O), t(7, k), t(14, Y), t(15, ue);
    });
  }
  const Je = () => {
    i("clear_status");
  };
  function Qe(y) {
    Ut[y ? "unshift" : "push"](() => {
      N = y, t(13, N);
    });
  }
  return l.$$set = (y) => {
    "i18n" in y && t(1, o = y.i18n), "eta" in y && t(0, u = y.eta), "queue_position" in y && t(2, a = y.queue_position), "queue_size" in y && t(3, r = y.queue_size), "status" in y && t(4, _ = y.status), "scroll_to_output" in y && t(22, c = y.scroll_to_output), "timer" in y && t(5, h = y.timer), "show_progress" in y && t(6, L = y.show_progress), "message" in y && t(23, M = y.message), "progress" in y && t(7, k = y.progress), "variant" in y && t(8, v = y.variant), "loading_text" in y && t(9, m = y.loading_text), "absolute" in y && t(10, b = y.absolute), "translucent" in y && t(11, C = y.translucent), "border" in y && t(12, T = y.border), "autoscroll" in y && t(24, p = y.autoscroll), "$$scope" in y && t(29, f = y.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (u === null && t(0, u = ne), u != null && ne !== u && (t(28, ie = (performance.now() - le) / 1e3 + u), t(19, pe = ie.toFixed(1)), t(27, ne = u))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, ge = ie === null || ie <= 0 || !j ? null : Math.min(j / ie, 1)), l.$$.dirty[0] & /*progress*/
    128 && k != null && t(18, we = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (k != null ? t(14, Y = k.map((y) => {
      if (y.index != null && y.length != null)
        return y.index / y.length;
      if (y.progress != null)
        return y.progress;
    })) : t(14, Y = null), Y ? (t(15, ue = Y[Y.length - 1]), O && (ue === 0 ? t(16, O.style.transition = "0", O) : t(16, O.style.transition = "150ms", O))) : t(15, ue = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? _e() : w()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && N && c && (_ === "pending" || _ === "complete") && $i(N, p), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = j.toFixed(1));
  }, [
    u,
    o,
    a,
    r,
    _,
    h,
    L,
    k,
    v,
    m,
    b,
    C,
    T,
    N,
    Y,
    ue,
    O,
    ge,
    we,
    pe,
    n,
    i,
    c,
    M,
    p,
    le,
    j,
    ne,
    ie,
    f,
    s,
    We,
    Je,
    Qe
  ];
}
class ts extends Ei {
  constructor(e) {
    super(), Ti(
      this,
      e,
      es,
      Qi,
      Bi,
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
  SvelteComponent: ls,
  add_iframe_resize_listener: ns,
  add_render_callback: is,
  append: ss,
  attr: fs,
  binding_callbacks: os,
  detach: as,
  element: us,
  init: rs,
  insert: _s,
  noop: ol,
  safe_not_equal: cs,
  set_data: ds,
  text: ms,
  toggle_class: qe
} = window.__gradio__svelte__internal, { onMount: hs } = window.__gradio__svelte__internal;
function bs(l) {
  let e, t = (
    /*value*/
    (l[0] ? (
      /*value*/
      l[0]
    ) : "") + ""
  ), n, s;
  return {
    c() {
      e = us("div"), n = ms(t), fs(e, "class", "svelte-84cxb8"), is(() => (
        /*div_elementresize_handler*/
        l[5].call(e)
      )), qe(
        e,
        "table",
        /*type*/
        l[1] === "table"
      ), qe(
        e,
        "gallery",
        /*type*/
        l[1] === "gallery"
      ), qe(
        e,
        "selected",
        /*selected*/
        l[2]
      );
    },
    m(f, i) {
      _s(f, e, i), ss(e, n), s = ns(
        e,
        /*div_elementresize_handler*/
        l[5].bind(e)
      ), l[6](e);
    },
    p(f, [i]) {
      i & /*value*/
      1 && t !== (t = /*value*/
      (f[0] ? (
        /*value*/
        f[0]
      ) : "") + "") && ds(n, t), i & /*type*/
      2 && qe(
        e,
        "table",
        /*type*/
        f[1] === "table"
      ), i & /*type*/
      2 && qe(
        e,
        "gallery",
        /*type*/
        f[1] === "gallery"
      ), i & /*selected*/
      4 && qe(
        e,
        "selected",
        /*selected*/
        f[2]
      );
    },
    i: ol,
    o: ol,
    d(f) {
      f && as(e), s(), l[6](null);
    }
  };
}
function gs(l, e, t) {
  let { value: n } = e, { type: s } = e, { selected: f = !1 } = e, i, o;
  function u(_, c) {
    !_ || !c || (o.style.setProperty("--local-text-width", `${c < 150 ? c : 200}px`), t(4, o.style.whiteSpace = "unset", o));
  }
  hs(() => {
    u(o, i);
  });
  function a() {
    i = this.clientWidth, t(3, i);
  }
  function r(_) {
    os[_ ? "unshift" : "push"](() => {
      o = _, t(4, o);
    });
  }
  return l.$$set = (_) => {
    "value" in _ && t(0, n = _.value), "type" in _ && t(1, s = _.type), "selected" in _ && t(2, f = _.selected);
  }, [n, s, f, i, o, a, r];
}
class zs extends ls {
  constructor(e) {
    super(), rs(this, e, gs, bs, cs, { value: 0, type: 1, selected: 2 });
  }
}
const {
  SvelteComponent: ws,
  add_flush_callback: al,
  assign: vs,
  bind: ul,
  binding_callbacks: rl,
  check_outros: ps,
  create_component: kt,
  destroy_component: Ct,
  detach: ks,
  flush: Z,
  get_spread_object: Cs,
  get_spread_update: ys,
  group_outros: Ls,
  init: Ms,
  insert: Vs,
  mount_component: yt,
  safe_not_equal: Hs,
  space: qs,
  transition_in: Ze,
  transition_out: Ne
} = window.__gradio__svelte__internal;
function _l(l) {
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
  for (let f = 0; f < n.length; f += 1)
    s = vs(s, n[f]);
  return e = new ts({ props: s }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[24]
  ), {
    c() {
      kt(e.$$.fragment);
    },
    m(f, i) {
      yt(e, f, i), t = !0;
    },
    p(f, i) {
      const o = i[0] & /*gradio, loading_status*/
      262148 ? ys(n, [
        i[0] & /*gradio*/
        4 && { autoscroll: (
          /*gradio*/
          f[2].autoscroll
        ) },
        i[0] & /*gradio*/
        4 && { i18n: (
          /*gradio*/
          f[2].i18n
        ) },
        i[0] & /*loading_status*/
        262144 && Cs(
          /*loading_status*/
          f[18]
        )
      ]) : {};
      e.$set(o);
    },
    i(f) {
      t || (Ze(e.$$.fragment, f), t = !0);
    },
    o(f) {
      Ne(e.$$.fragment, f), t = !1;
    },
    d(f) {
      Ct(e, f);
    }
  };
}
function Fs(l) {
  let e, t, n, s, f, i = (
    /*loading_status*/
    l[18] && _l(l)
  );
  function o(r) {
    l[25](r);
  }
  function u(r) {
    l[26](r);
  }
  let a = {
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
    l[0] !== void 0 && (a.value = /*value*/
    l[0]), /*value_is_output*/
    l[1] !== void 0 && (a.value_is_output = /*value_is_output*/
    l[1]), t = new Ci({ props: a }), rl.push(() => ul(t, "value", o)), rl.push(() => ul(t, "value_is_output", u)), t.$on(
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
        i && i.c(), e = qs(), kt(t.$$.fragment);
      },
      m(r, _) {
        i && i.m(r, _), Vs(r, e, _), yt(t, r, _), f = !0;
      },
      p(r, _) {
        /*loading_status*/
        r[18] ? i ? (i.p(r, _), _[0] & /*loading_status*/
        262144 && Ze(i, 1)) : (i = _l(r), i.c(), Ze(i, 1), i.m(e.parentNode, e)) : i && (Ls(), Ne(i, 1, 1, () => {
          i = null;
        }), ps());
        const c = {};
        _[0] & /*label*/
        8 && (c.label = /*label*/
        r[3]), _[0] & /*info*/
        16 && (c.info = /*info*/
        r[4]), _[0] & /*show_label*/
        1024 && (c.show_label = /*show_label*/
        r[10]), _[0] & /*lines*/
        256 && (c.lines = /*lines*/
        r[8]), _[0] & /*type*/
        16384 && (c.type = /*type*/
        r[14]), _[0] & /*rtl*/
        524288 && (c.rtl = /*rtl*/
        r[19]), _[0] & /*text_align*/
        1048576 && (c.text_align = /*text_align*/
        r[20]), _[0] & /*max_lines, lines*/
        2304 && (c.max_lines = /*max_lines*/
        r[11] ? (
          /*max_lines*/
          r[11]
        ) : (
          /*lines*/
          r[8] + 1
        )), _[0] & /*prompts*/
        4096 && (c.prompts = /*prompts*/
        r[12]), _[0] & /*suffixes*/
        8192 && (c.suffixes = /*suffixes*/
        r[13]), _[0] & /*placeholder*/
        512 && (c.placeholder = /*placeholder*/
        r[9]), _[0] & /*autofocus*/
        2097152 && (c.autofocus = /*autofocus*/
        r[21]), _[0] & /*container*/
        32768 && (c.container = /*container*/
        r[15]), _[0] & /*autoscroll*/
        4194304 && (c.autoscroll = /*autoscroll*/
        r[22]), _[0] & /*interactive*/
        8388608 && (c.disabled = !/*interactive*/
        r[23]), !n && _[0] & /*value*/
        1 && (n = !0, c.value = /*value*/
        r[0], al(() => n = !1)), !s && _[0] & /*value_is_output*/
        2 && (s = !0, c.value_is_output = /*value_is_output*/
        r[1], al(() => s = !1)), t.$set(c);
      },
      i(r) {
        f || (Ze(i), Ze(t.$$.fragment, r), f = !0);
      },
      o(r) {
        Ne(i), Ne(t.$$.fragment, r), f = !1;
      },
      d(r) {
        r && ks(e), i && i.d(r), Ct(t, r);
      }
    }
  );
}
function Zs(l) {
  let e, t;
  return e = new Ul({
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
      $$slots: { default: [Fs] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      kt(e.$$.fragment);
    },
    m(n, s) {
      yt(e, n, s), t = !0;
    },
    p(n, s) {
      const f = {};
      s[0] & /*visible*/
      128 && (f.visible = /*visible*/
      n[7]), s[0] & /*elem_id*/
      32 && (f.elem_id = /*elem_id*/
      n[5]), s[0] & /*elem_classes*/
      64 && (f.elem_classes = /*elem_classes*/
      n[6]), s[0] & /*scale*/
      65536 && (f.scale = /*scale*/
      n[16]), s[0] & /*min_width*/
      131072 && (f.min_width = /*min_width*/
      n[17]), s[0] & /*container*/
      32768 && (f.padding = /*container*/
      n[15]), s[0] & /*label, info, show_label, lines, type, rtl, text_align, max_lines, prompts, suffixes, placeholder, autofocus, container, autoscroll, interactive, value, value_is_output, gradio, loading_status*/
      16580383 | s[1] & /*$$scope*/
      4 && (f.$$scope = { dirty: s, ctx: n }), e.$set(f);
    },
    i(n) {
      t || (Ze(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ne(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Ct(e, n);
    }
  };
}
function Ss(l, e, t) {
  let { gradio: n } = e, { label: s = "Textbox" } = e, { info: f = void 0 } = e, { elem_id: i = "" } = e, { elem_classes: o = [] } = e, { visible: u = !0 } = e, { value: a = "" } = e, { lines: r } = e, { placeholder: _ = "" } = e, { show_label: c } = e, { max_lines: h } = e, { prompts: L = [] } = e, { suffixes: M = [] } = e, { type: k = "text" } = e, { container: v = !0 } = e, { scale: m = null } = e, { min_width: b = void 0 } = e, { loading_status: C = void 0 } = e, { value_is_output: T = !1 } = e, { rtl: p = !1 } = e, { text_align: N = void 0 } = e, { autofocus: I = !1 } = e, { autoscroll: le = !0 } = e, { interactive: j = !0 } = e;
  const ne = () => n.dispatch("clear_status", C);
  function ie(w) {
    a = w, t(0, a);
  }
  function ge(w) {
    T = w, t(1, T);
  }
  const Y = () => n.dispatch("change", a), ue = () => n.dispatch("input"), O = () => n.dispatch("submit"), we = () => n.dispatch("blur"), _e = (w) => n.dispatch("select", w.detail), ve = () => n.dispatch("focus");
  return l.$$set = (w) => {
    "gradio" in w && t(2, n = w.gradio), "label" in w && t(3, s = w.label), "info" in w && t(4, f = w.info), "elem_id" in w && t(5, i = w.elem_id), "elem_classes" in w && t(6, o = w.elem_classes), "visible" in w && t(7, u = w.visible), "value" in w && t(0, a = w.value), "lines" in w && t(8, r = w.lines), "placeholder" in w && t(9, _ = w.placeholder), "show_label" in w && t(10, c = w.show_label), "max_lines" in w && t(11, h = w.max_lines), "prompts" in w && t(12, L = w.prompts), "suffixes" in w && t(13, M = w.suffixes), "type" in w && t(14, k = w.type), "container" in w && t(15, v = w.container), "scale" in w && t(16, m = w.scale), "min_width" in w && t(17, b = w.min_width), "loading_status" in w && t(18, C = w.loading_status), "value_is_output" in w && t(1, T = w.value_is_output), "rtl" in w && t(19, p = w.rtl), "text_align" in w && t(20, N = w.text_align), "autofocus" in w && t(21, I = w.autofocus), "autoscroll" in w && t(22, le = w.autoscroll), "interactive" in w && t(23, j = w.interactive);
  }, [
    a,
    T,
    n,
    s,
    f,
    i,
    o,
    u,
    r,
    _,
    c,
    h,
    L,
    M,
    k,
    v,
    m,
    b,
    C,
    p,
    N,
    I,
    le,
    j,
    ne,
    ie,
    ge,
    Y,
    ue,
    O,
    we,
    _e,
    ve
  ];
}
class Es extends ws {
  constructor(e) {
    super(), Ms(
      this,
      e,
      Ss,
      Zs,
      Hs,
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
    this.$$set({ gradio: e }), Z();
  }
  get label() {
    return this.$$.ctx[3];
  }
  set label(e) {
    this.$$set({ label: e }), Z();
  }
  get info() {
    return this.$$.ctx[4];
  }
  set info(e) {
    this.$$set({ info: e }), Z();
  }
  get elem_id() {
    return this.$$.ctx[5];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), Z();
  }
  get elem_classes() {
    return this.$$.ctx[6];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), Z();
  }
  get visible() {
    return this.$$.ctx[7];
  }
  set visible(e) {
    this.$$set({ visible: e }), Z();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), Z();
  }
  get lines() {
    return this.$$.ctx[8];
  }
  set lines(e) {
    this.$$set({ lines: e }), Z();
  }
  get placeholder() {
    return this.$$.ctx[9];
  }
  set placeholder(e) {
    this.$$set({ placeholder: e }), Z();
  }
  get show_label() {
    return this.$$.ctx[10];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), Z();
  }
  get max_lines() {
    return this.$$.ctx[11];
  }
  set max_lines(e) {
    this.$$set({ max_lines: e }), Z();
  }
  get prompts() {
    return this.$$.ctx[12];
  }
  set prompts(e) {
    this.$$set({ prompts: e }), Z();
  }
  get suffixes() {
    return this.$$.ctx[13];
  }
  set suffixes(e) {
    this.$$set({ suffixes: e }), Z();
  }
  get type() {
    return this.$$.ctx[14];
  }
  set type(e) {
    this.$$set({ type: e }), Z();
  }
  get container() {
    return this.$$.ctx[15];
  }
  set container(e) {
    this.$$set({ container: e }), Z();
  }
  get scale() {
    return this.$$.ctx[16];
  }
  set scale(e) {
    this.$$set({ scale: e }), Z();
  }
  get min_width() {
    return this.$$.ctx[17];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), Z();
  }
  get loading_status() {
    return this.$$.ctx[18];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), Z();
  }
  get value_is_output() {
    return this.$$.ctx[1];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), Z();
  }
  get rtl() {
    return this.$$.ctx[19];
  }
  set rtl(e) {
    this.$$set({ rtl: e }), Z();
  }
  get text_align() {
    return this.$$.ctx[20];
  }
  set text_align(e) {
    this.$$set({ text_align: e }), Z();
  }
  get autofocus() {
    return this.$$.ctx[21];
  }
  set autofocus(e) {
    this.$$set({ autofocus: e }), Z();
  }
  get autoscroll() {
    return this.$$.ctx[22];
  }
  set autoscroll(e) {
    this.$$set({ autoscroll: e }), Z();
  }
  get interactive() {
    return this.$$.ctx[23];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), Z();
  }
}
export {
  zs as BaseExample,
  Ci as BaseTextbox,
  Es as default
};
