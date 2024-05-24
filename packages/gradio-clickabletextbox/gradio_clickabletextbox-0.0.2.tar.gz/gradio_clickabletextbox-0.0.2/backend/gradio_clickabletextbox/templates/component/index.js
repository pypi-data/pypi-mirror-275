const {
  SvelteComponent: Sl,
  assign: zl,
  create_slot: El,
  detach: Tl,
  element: Bl,
  get_all_dirty_from_scope: Nl,
  get_slot_changes: Dl,
  get_spread_update: Il,
  init: jl,
  insert: Al,
  safe_not_equal: Pl,
  set_dynamic_element_data: Mt,
  set_style: K,
  toggle_class: ie,
  transition_in: dl,
  transition_out: ml,
  update_slot_base: Yl
} = window.__gradio__svelte__internal;
function Kl(l) {
  let e, t, n;
  const s = (
    /*#slots*/
    l[18].default
  ), o = El(
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
  ], f = {};
  for (let r = 0; r < i.length; r += 1)
    f = zl(f, i[r]);
  return {
    c() {
      e = Bl(
        /*tag*/
        l[14]
      ), o && o.c(), Mt(
        /*tag*/
        l[14]
      )(e, f), ie(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), ie(
        e,
        "padded",
        /*padding*/
        l[6]
      ), ie(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), ie(
        e,
        "border_contrast",
        /*border_mode*/
        l[5] === "contrast"
      ), ie(e, "hide-container", !/*explicit_call*/
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
    m(r, a) {
      Al(r, e, a), o && o.m(e, null), n = !0;
    },
    p(r, a) {
      o && o.p && (!n || a & /*$$scope*/
      131072) && Yl(
        o,
        s,
        r,
        /*$$scope*/
        r[17],
        n ? Dl(
          s,
          /*$$scope*/
          r[17],
          a,
          null
        ) : Nl(
          /*$$scope*/
          r[17]
        ),
        null
      ), Mt(
        /*tag*/
        r[14]
      )(e, f = Il(i, [
        (!n || a & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!n || a & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!n || a & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), ie(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), ie(
        e,
        "padded",
        /*padding*/
        r[6]
      ), ie(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), ie(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), ie(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), a & /*height*/
      1 && K(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), a & /*width*/
      2 && K(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), a & /*variant*/
      16 && K(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), a & /*allow_overflow*/
      2048 && K(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), a & /*scale*/
      4096 && K(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), a & /*min_width*/
      8192 && K(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      n || (dl(o, r), n = !0);
    },
    o(r) {
      ml(o, r), n = !1;
    },
    d(r) {
      r && Tl(e), o && o.d(r);
    }
  };
}
function Ol(l) {
  let e, t = (
    /*tag*/
    l[14] && Kl(l)
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
      e || (dl(t, n), e = !0);
    },
    o(n) {
      ml(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function Ul(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { height: o = void 0 } = e, { width: i = void 0 } = e, { elem_id: f = "" } = e, { elem_classes: r = [] } = e, { variant: a = "solid" } = e, { border_mode: u = "base" } = e, { padding: _ = !0 } = e, { type: c = "normal" } = e, { test_id: h = void 0 } = e, { explicit_call: L = !1 } = e, { container: H = !0 } = e, { visible: p = !0 } = e, { allow_overflow: v = !0 } = e, { scale: m = null } = e, { min_width: b = 0 } = e, C = c === "fieldset" ? "fieldset" : "div";
  const T = (k) => {
    if (k !== void 0) {
      if (typeof k == "number")
        return k + "px";
      if (typeof k == "string")
        return k;
    }
  };
  return l.$$set = (k) => {
    "height" in k && t(0, o = k.height), "width" in k && t(1, i = k.width), "elem_id" in k && t(2, f = k.elem_id), "elem_classes" in k && t(3, r = k.elem_classes), "variant" in k && t(4, a = k.variant), "border_mode" in k && t(5, u = k.border_mode), "padding" in k && t(6, _ = k.padding), "type" in k && t(16, c = k.type), "test_id" in k && t(7, h = k.test_id), "explicit_call" in k && t(8, L = k.explicit_call), "container" in k && t(9, H = k.container), "visible" in k && t(10, p = k.visible), "allow_overflow" in k && t(11, v = k.allow_overflow), "scale" in k && t(12, m = k.scale), "min_width" in k && t(13, b = k.min_width), "$$scope" in k && t(17, s = k.$$scope);
  }, [
    o,
    i,
    f,
    r,
    a,
    u,
    _,
    h,
    L,
    H,
    p,
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
class Xl extends Sl {
  constructor(e) {
    super(), jl(this, e, Ul, Ol, Pl, {
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
  SvelteComponent: Gl,
  attr: Rl,
  create_slot: Wl,
  detach: Jl,
  element: Ql,
  get_all_dirty_from_scope: xl,
  get_slot_changes: $l,
  init: en,
  insert: tn,
  safe_not_equal: ln,
  transition_in: nn,
  transition_out: sn,
  update_slot_base: on
} = window.__gradio__svelte__internal;
function fn(l) {
  let e, t;
  const n = (
    /*#slots*/
    l[1].default
  ), s = Wl(
    n,
    l,
    /*$$scope*/
    l[0],
    null
  );
  return {
    c() {
      e = Ql("div"), s && s.c(), Rl(e, "class", "svelte-1hnfib2");
    },
    m(o, i) {
      tn(o, e, i), s && s.m(e, null), t = !0;
    },
    p(o, [i]) {
      s && s.p && (!t || i & /*$$scope*/
      1) && on(
        s,
        n,
        o,
        /*$$scope*/
        o[0],
        t ? $l(
          n,
          /*$$scope*/
          o[0],
          i,
          null
        ) : xl(
          /*$$scope*/
          o[0]
        ),
        null
      );
    },
    i(o) {
      t || (nn(s, o), t = !0);
    },
    o(o) {
      sn(s, o), t = !1;
    },
    d(o) {
      o && Jl(e), s && s.d(o);
    }
  };
}
function an(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e;
  return l.$$set = (o) => {
    "$$scope" in o && t(0, s = o.$$scope);
  }, [s, n];
}
class rn extends Gl {
  constructor(e) {
    super(), en(this, e, an, fn, ln, {});
  }
}
const {
  SvelteComponent: un,
  attr: Vt,
  check_outros: _n,
  create_component: cn,
  create_slot: dn,
  destroy_component: mn,
  detach: Pe,
  element: hn,
  empty: bn,
  get_all_dirty_from_scope: gn,
  get_slot_changes: wn,
  group_outros: vn,
  init: kn,
  insert: Ye,
  mount_component: pn,
  safe_not_equal: Cn,
  set_data: yn,
  space: Ln,
  text: Mn,
  toggle_class: Le,
  transition_in: Be,
  transition_out: Ke,
  update_slot_base: Vn
} = window.__gradio__svelte__internal;
function Ht(l) {
  let e, t;
  return e = new rn({
    props: {
      $$slots: { default: [Hn] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      cn(e.$$.fragment);
    },
    m(n, s) {
      pn(e, n, s), t = !0;
    },
    p(n, s) {
      const o = {};
      s & /*$$scope, info*/
      10 && (o.$$scope = { dirty: s, ctx: n }), e.$set(o);
    },
    i(n) {
      t || (Be(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ke(e.$$.fragment, n), t = !1;
    },
    d(n) {
      mn(e, n);
    }
  };
}
function Hn(l) {
  let e;
  return {
    c() {
      e = Mn(
        /*info*/
        l[1]
      );
    },
    m(t, n) {
      Ye(t, e, n);
    },
    p(t, n) {
      n & /*info*/
      2 && yn(
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
function qn(l) {
  let e, t, n, s;
  const o = (
    /*#slots*/
    l[2].default
  ), i = dn(
    o,
    l,
    /*$$scope*/
    l[3],
    null
  );
  let f = (
    /*info*/
    l[1] && Ht(l)
  );
  return {
    c() {
      e = hn("span"), i && i.c(), t = Ln(), f && f.c(), n = bn(), Vt(e, "data-testid", "block-info"), Vt(e, "class", "svelte-22c38v"), Le(e, "sr-only", !/*show_label*/
      l[0]), Le(e, "hide", !/*show_label*/
      l[0]), Le(
        e,
        "has-info",
        /*info*/
        l[1] != null
      );
    },
    m(r, a) {
      Ye(r, e, a), i && i.m(e, null), Ye(r, t, a), f && f.m(r, a), Ye(r, n, a), s = !0;
    },
    p(r, [a]) {
      i && i.p && (!s || a & /*$$scope*/
      8) && Vn(
        i,
        o,
        r,
        /*$$scope*/
        r[3],
        s ? wn(
          o,
          /*$$scope*/
          r[3],
          a,
          null
        ) : gn(
          /*$$scope*/
          r[3]
        ),
        null
      ), (!s || a & /*show_label*/
      1) && Le(e, "sr-only", !/*show_label*/
      r[0]), (!s || a & /*show_label*/
      1) && Le(e, "hide", !/*show_label*/
      r[0]), (!s || a & /*info*/
      2) && Le(
        e,
        "has-info",
        /*info*/
        r[1] != null
      ), /*info*/
      r[1] ? f ? (f.p(r, a), a & /*info*/
      2 && Be(f, 1)) : (f = Ht(r), f.c(), Be(f, 1), f.m(n.parentNode, n)) : f && (vn(), Ke(f, 1, 1, () => {
        f = null;
      }), _n());
    },
    i(r) {
      s || (Be(i, r), Be(f), s = !0);
    },
    o(r) {
      Ke(i, r), Ke(f), s = !1;
    },
    d(r) {
      r && (Pe(e), Pe(t), Pe(n)), i && i.d(r), f && f.d(r);
    }
  };
}
function Fn(l, e, t) {
  let { $$slots: n = {}, $$scope: s } = e, { show_label: o = !0 } = e, { info: i = void 0 } = e;
  return l.$$set = (f) => {
    "show_label" in f && t(0, o = f.show_label), "info" in f && t(1, i = f.info), "$$scope" in f && t(3, s = f.$$scope);
  }, [o, i, n, s];
}
class Zn extends un {
  constructor(e) {
    super(), kn(this, e, Fn, qn, Cn, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: Sn,
  append: ut,
  attr: ue,
  bubble: zn,
  create_component: En,
  destroy_component: Tn,
  detach: hl,
  element: _t,
  init: Bn,
  insert: bl,
  listen: Nn,
  mount_component: Dn,
  safe_not_equal: In,
  set_data: jn,
  set_style: Me,
  space: An,
  text: Pn,
  toggle_class: P,
  transition_in: Yn,
  transition_out: Kn
} = window.__gradio__svelte__internal;
function qt(l) {
  let e, t;
  return {
    c() {
      e = _t("span"), t = Pn(
        /*label*/
        l[1]
      ), ue(e, "class", "svelte-1lrphxw");
    },
    m(n, s) {
      bl(n, e, s), ut(e, t);
    },
    p(n, s) {
      s & /*label*/
      2 && jn(
        t,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && hl(e);
    }
  };
}
function On(l) {
  let e, t, n, s, o, i, f, r = (
    /*show_label*/
    l[2] && qt(l)
  );
  return s = new /*Icon*/
  l[0]({}), {
    c() {
      e = _t("button"), r && r.c(), t = An(), n = _t("div"), En(s.$$.fragment), ue(n, "class", "svelte-1lrphxw"), P(
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
      l[7], ue(
        e,
        "aria-label",
        /*label*/
        l[1]
      ), ue(
        e,
        "aria-haspopup",
        /*hasPopup*/
        l[8]
      ), ue(
        e,
        "title",
        /*label*/
        l[1]
      ), ue(e, "class", "svelte-1lrphxw"), P(
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
    m(a, u) {
      bl(a, e, u), r && r.m(e, null), ut(e, t), ut(e, n), Dn(s, n, null), o = !0, i || (f = Nn(
        e,
        "click",
        /*click_handler*/
        l[14]
      ), i = !0);
    },
    p(a, [u]) {
      /*show_label*/
      a[2] ? r ? r.p(a, u) : (r = qt(a), r.c(), r.m(e, t)) : r && (r.d(1), r = null), (!o || u & /*size*/
      16) && P(
        n,
        "small",
        /*size*/
        a[4] === "small"
      ), (!o || u & /*size*/
      16) && P(
        n,
        "large",
        /*size*/
        a[4] === "large"
      ), (!o || u & /*size*/
      16) && P(
        n,
        "medium",
        /*size*/
        a[4] === "medium"
      ), (!o || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      a[7]), (!o || u & /*label*/
      2) && ue(
        e,
        "aria-label",
        /*label*/
        a[1]
      ), (!o || u & /*hasPopup*/
      256) && ue(
        e,
        "aria-haspopup",
        /*hasPopup*/
        a[8]
      ), (!o || u & /*label*/
      2) && ue(
        e,
        "title",
        /*label*/
        a[1]
      ), (!o || u & /*pending*/
      8) && P(
        e,
        "pending",
        /*pending*/
        a[3]
      ), (!o || u & /*padded*/
      32) && P(
        e,
        "padded",
        /*padded*/
        a[5]
      ), (!o || u & /*highlight*/
      64) && P(
        e,
        "highlight",
        /*highlight*/
        a[6]
      ), (!o || u & /*transparent*/
      512) && P(
        e,
        "transparent",
        /*transparent*/
        a[9]
      ), u & /*disabled, _color*/
      4224 && Me(e, "color", !/*disabled*/
      a[7] && /*_color*/
      a[12] ? (
        /*_color*/
        a[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && Me(e, "--bg-color", /*disabled*/
      a[7] ? "auto" : (
        /*background*/
        a[10]
      )), u & /*offset*/
      2048 && Me(
        e,
        "margin-left",
        /*offset*/
        a[11] + "px"
      );
    },
    i(a) {
      o || (Yn(s.$$.fragment, a), o = !0);
    },
    o(a) {
      Kn(s.$$.fragment, a), o = !1;
    },
    d(a) {
      a && hl(e), r && r.d(), Tn(s), i = !1, f();
    }
  };
}
function Un(l, e, t) {
  let n, { Icon: s } = e, { label: o = "" } = e, { show_label: i = !1 } = e, { pending: f = !1 } = e, { size: r = "small" } = e, { padded: a = !0 } = e, { highlight: u = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: c = !1 } = e, { color: h = "var(--block-label-text-color)" } = e, { transparent: L = !1 } = e, { background: H = "var(--background-fill-primary)" } = e, { offset: p = 0 } = e;
  function v(m) {
    zn.call(this, l, m);
  }
  return l.$$set = (m) => {
    "Icon" in m && t(0, s = m.Icon), "label" in m && t(1, o = m.label), "show_label" in m && t(2, i = m.show_label), "pending" in m && t(3, f = m.pending), "size" in m && t(4, r = m.size), "padded" in m && t(5, a = m.padded), "highlight" in m && t(6, u = m.highlight), "disabled" in m && t(7, _ = m.disabled), "hasPopup" in m && t(8, c = m.hasPopup), "color" in m && t(13, h = m.color), "transparent" in m && t(9, L = m.transparent), "background" in m && t(10, H = m.background), "offset" in m && t(11, p = m.offset);
  }, l.$$.update = () => {
    l.$$.dirty & /*highlight, color*/
    8256 && t(12, n = u ? "var(--color-accent)" : h);
  }, [
    s,
    o,
    i,
    f,
    r,
    a,
    u,
    _,
    c,
    L,
    H,
    p,
    n,
    h,
    v
  ];
}
class Xn extends Sn {
  constructor(e) {
    super(), Bn(this, e, Un, On, In, {
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
  SvelteComponent: Gn,
  append: it,
  attr: R,
  detach: Rn,
  init: Wn,
  insert: Jn,
  noop: st,
  safe_not_equal: Qn,
  set_style: se,
  svg_element: Ie
} = window.__gradio__svelte__internal;
function xn(l) {
  let e, t, n, s;
  return {
    c() {
      e = Ie("svg"), t = Ie("g"), n = Ie("path"), s = Ie("path"), R(n, "d", "M18,6L6.087,17.913"), se(n, "fill", "none"), se(n, "fill-rule", "nonzero"), se(n, "stroke-width", "2px"), R(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), R(s, "d", "M4.364,4.364L19.636,19.636"), se(s, "fill", "none"), se(s, "fill-rule", "nonzero"), se(s, "stroke-width", "2px"), R(e, "width", "100%"), R(e, "height", "100%"), R(e, "viewBox", "0 0 24 24"), R(e, "version", "1.1"), R(e, "xmlns", "http://www.w3.org/2000/svg"), R(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), R(e, "xml:space", "preserve"), R(e, "stroke", "currentColor"), se(e, "fill-rule", "evenodd"), se(e, "clip-rule", "evenodd"), se(e, "stroke-linecap", "round"), se(e, "stroke-linejoin", "round");
    },
    m(o, i) {
      Jn(o, e, i), it(e, t), it(t, n), it(e, s);
    },
    p: st,
    i: st,
    o: st,
    d(o) {
      o && Rn(e);
    }
  };
}
class $n extends Gn {
  constructor(e) {
    super(), Wn(this, e, null, xn, Qn, {});
  }
}
const ei = [
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
], Ft = {
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
ei.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: Ft[e][t],
      secondary: Ft[e][n]
    }
  }),
  {}
);
function Oe() {
}
function ti(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const gl = typeof window < "u";
let Zt = gl ? () => window.performance.now() : () => Date.now(), wl = gl ? (l) => requestAnimationFrame(l) : Oe;
const Se = /* @__PURE__ */ new Set();
function vl(l) {
  Se.forEach((e) => {
    e.c(l) || (Se.delete(e), e.f());
  }), Se.size !== 0 && wl(vl);
}
function li(l) {
  let e;
  return Se.size === 0 && wl(vl), {
    promise: new Promise((t) => {
      Se.add(e = { c: l, f: t });
    }),
    abort() {
      Se.delete(e);
    }
  };
}
function ni(l) {
  const e = l - 1;
  return e * e * e + 1;
}
const Ve = [];
function ii(l, e = Oe) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function s(f) {
    if (ti(l, f) && (l = f, t)) {
      const r = !Ve.length;
      for (const a of n)
        a[1](), Ve.push(a, l);
      if (r) {
        for (let a = 0; a < Ve.length; a += 2)
          Ve[a][0](Ve[a + 1]);
        Ve.length = 0;
      }
    }
  }
  function o(f) {
    s(f(l));
  }
  function i(f, r = Oe) {
    const a = [f, r];
    return n.add(a), n.size === 1 && (t = e(s, o) || Oe), f(l), () => {
      n.delete(a), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: s, update: o, subscribe: i };
}
function St(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function ct(l, e, t, n) {
  if (typeof t == "number" || St(t)) {
    const s = n - t, o = (t - e) / (l.dt || 1 / 60), i = l.opts.stiffness * s, f = l.opts.damping * o, r = (i - f) * l.inv_mass, a = (o + r) * l.dt;
    return Math.abs(a) < l.opts.precision && Math.abs(s) < l.opts.precision ? n : (l.settled = !1, St(t) ? new Date(t.getTime() + a) : t + a);
  } else {
    if (Array.isArray(t))
      return t.map(
        (s, o) => ct(l, e[o], t[o], n[o])
      );
    if (typeof t == "object") {
      const s = {};
      for (const o in t)
        s[o] = ct(l, e[o], t[o], n[o]);
      return s;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function zt(l, e = {}) {
  const t = ii(l), { stiffness: n = 0.15, damping: s = 0.8, precision: o = 0.01 } = e;
  let i, f, r, a = l, u = l, _ = 1, c = 0, h = !1;
  function L(p, v = {}) {
    u = p;
    const m = r = {};
    return l == null || v.hard || H.stiffness >= 1 && H.damping >= 1 ? (h = !0, i = Zt(), a = p, t.set(l = u), Promise.resolve()) : (v.soft && (c = 1 / ((v.soft === !0 ? 0.5 : +v.soft) * 60), _ = 0), f || (i = Zt(), h = !1, f = li((b) => {
      if (h)
        return h = !1, f = null, !1;
      _ = Math.min(_ + c, 1);
      const C = {
        inv_mass: _,
        opts: H,
        settled: !0,
        dt: (b - i) * 60 / 1e3
      }, T = ct(C, a, l, u);
      return i = b, a = l, t.set(l = T), C.settled && (f = null), !C.settled;
    })), new Promise((b) => {
      f.promise.then(() => {
        m === r && b();
      });
    }));
  }
  const H = {
    set: L,
    update: (p, v) => L(p(u, l), v),
    subscribe: t.subscribe,
    stiffness: n,
    damping: s,
    precision: o
  };
  return H;
}
function Et(l, { delay: e = 0, duration: t = 500, easing: n = ni } = {}) {
  const s = parseFloat(getComputedStyle(l).height);
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (o) => {
      const i = o, f = `translateY(${(1 - o) * -10}px)`, r = o * s;
      return `
                opacity: ${i};
                transform: ${f};
                height: ${r}px;
            `;
    }
  };
}
const {
  SvelteComponent: si,
  action_destroyer: bt,
  add_render_callback: oi,
  append: F,
  attr: g,
  binding_callbacks: ot,
  bubble: He,
  check_outros: fi,
  create_bidirectional_transition: Tt,
  create_component: ai,
  destroy_component: ri,
  destroy_each: kl,
  detach: $,
  element: B,
  ensure_array_like: Ue,
  group_outros: ui,
  init: _i,
  insert: ee,
  is_function: gt,
  listen: E,
  mount_component: ci,
  noop: Xe,
  null_to_empty: wt,
  run_all: vt,
  safe_not_equal: di,
  set_data: kt,
  set_input_value: ze,
  space: te,
  svg_element: Ge,
  text: pt,
  toggle_class: Bt,
  transition_in: ft,
  transition_out: at
} = window.__gradio__svelte__internal, { beforeUpdate: mi, afterUpdate: hi, createEventDispatcher: bi, tick: Nt } = window.__gradio__svelte__internal;
function Dt(l, e, t) {
  const n = l.slice();
  return n[47] = e[t], n;
}
function It(l, e, t) {
  const n = l.slice();
  return n[47] = e[t], n;
}
function gi(l) {
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
      8 && kt(
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
function wi(l) {
  let e, t, n, s, o, i;
  return {
    c() {
      e = B("textarea"), g(e, "data-testid", "textbox"), g(e, "class", wt(
        /*show_magic*/
        l[15] ? "scroll_hide_magic" : "scroll-hide"
      ) + " svelte-82ixrs"), g(e, "dir", t = /*rtl*/
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
    m(f, r) {
      ee(f, e, r), ze(
        e,
        /*value*/
        l[0]
      ), l[38](e), /*autofocus*/
      l[11] && e.focus(), o || (i = [
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
      ], o = !0);
    },
    p(f, r) {
      r[0] & /*rtl*/
      1024 && t !== (t = /*rtl*/
      f[10] ? "rtl" : "ltr") && g(e, "dir", t), r[0] & /*placeholder*/
      4 && g(
        e,
        "placeholder",
        /*placeholder*/
        f[2]
      ), r[0] & /*lines*/
      2 && g(
        e,
        "rows",
        /*lines*/
        f[1]
      ), r[0] & /*disabled*/
      32 && (e.disabled = /*disabled*/
      f[5]), r[0] & /*autofocus*/
      2048 && (e.autofocus = /*autofocus*/
      f[11]), r[0] & /*text_align*/
      4096 && n !== (n = /*text_align*/
      f[12] ? "text-align: " + /*text_align*/
      f[12] : "") && g(e, "style", n), s && gt(s.update) && r[0] & /*value*/
      1 && s.update.call(
        null,
        /*value*/
        f[0]
      ), r[0] & /*value*/
      1 && ze(
        e,
        /*value*/
        f[0]
      );
    },
    i: Xe,
    o: Xe,
    d(f) {
      f && $(e), l[38](null), o = !1, vt(i);
    }
  };
}
function vi(l) {
  let e, t, n, s, o, i, f, r, a;
  return {
    c() {
      e = B("div"), t = B("textarea"), i = te(), f = B("button"), f.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-82ixrs"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#CCCCCC" class="svelte-82ixrs"></path></svg>', g(t, "data-testid", "textbox"), g(t, "class", wt(
        /*show_magic*/
        l[15] ? "scroll_hide_magic" : "scroll-hide"
      ) + " svelte-82ixrs"), g(t, "dir", n = /*rtl*/
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
      l[12] : ""), g(f, "class", "extend_button svelte-82ixrs"), g(f, "aria-label", "Extend"), g(f, "aria-roledescription", "Extend text"), g(e, "class", "magic_container svelte-82ixrs");
    },
    m(u, _) {
      ee(u, e, _), F(e, t), ze(
        t,
        /*value*/
        l[0]
      ), l[36](t), F(e, i), F(e, f), /*autofocus*/
      l[11] && t.focus(), r || (a = [
        bt(o = /*text_area_resize*/
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
          f,
          "click",
          /*handle_extension*/
          l[16]
        )
      ], r = !0);
    },
    p(u, _) {
      _[0] & /*rtl*/
      1024 && n !== (n = /*rtl*/
      u[10] ? "rtl" : "ltr") && g(t, "dir", n), _[0] & /*placeholder*/
      4 && g(
        t,
        "placeholder",
        /*placeholder*/
        u[2]
      ), _[0] & /*lines*/
      2 && g(
        t,
        "rows",
        /*lines*/
        u[1]
      ), _[0] & /*disabled*/
      32 && (t.disabled = /*disabled*/
      u[5]), _[0] & /*autofocus*/
      2048 && (t.autofocus = /*autofocus*/
      u[11]), _[0] & /*text_align*/
      4096 && s !== (s = /*text_align*/
      u[12] ? "text-align: " + /*text_align*/
      u[12] : "") && g(t, "style", s), o && gt(o.update) && _[0] & /*value*/
      1 && o.update.call(
        null,
        /*value*/
        u[0]
      ), _[0] & /*value*/
      1 && ze(
        t,
        /*value*/
        u[0]
      );
    },
    i: Xe,
    o: Xe,
    d(u) {
      u && $(e), l[36](null), r = !1, vt(a);
    }
  };
}
function ki(l) {
  let e, t, n, s, o, i, f, r, a, u, _, c, h, L, H = (
    /*prompts*/
    l[8].length > 0 && jt(l)
  ), p = (
    /*suffixes*/
    l[9].length > 0 && Pt(l)
  );
  return {
    c() {
      e = B("div"), t = B("textarea"), i = te(), f = B("button"), f.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-82ixrs"><path d="M23.0978 15.6987L23.5777 15.2188L21.7538 13.3952L21.2739 13.8751L23.0978 15.6987ZM11.1253 2.74873L10.6454 3.22809L12.4035 4.98733L12.8834 4.50769L11.1253 2.74873ZM25.5996 9.23801H22.885V9.91673H25.5996V9.23801ZM10.6692 9.23801H7.95457V9.91673H10.6692V9.23801ZM21.8008 5.01533L23.5982 3.21773L23.118 2.73781L21.3206 4.53541L21.8008 5.01533ZM17.2391 7.29845L18.6858 8.74521C18.7489 8.80822 18.7989 8.88303 18.8331 8.96538C18.8672 9.04773 18.8847 9.13599 18.8847 9.22513C18.8847 9.31427 18.8672 9.40254 18.8331 9.48488C18.7989 9.56723 18.7489 9.64205 18.6858 9.70505L3.00501 25.3859C2.74013 25.6511 2.31061 25.6511 2.04517 25.3859L0.598406 23.9391C0.535351 23.8761 0.485329 23.8013 0.4512 23.719C0.417072 23.6366 0.399506 23.5483 0.399506 23.4592C0.399506 23.3701 0.417072 23.2818 0.4512 23.1995C0.485329 23.1171 0.535351 23.0423 0.598406 22.9793L16.2792 7.29845C16.3422 7.23533 16.417 7.18525 16.4994 7.15108C16.5817 7.11691 16.67 7.09932 16.7592 7.09932C16.8483 7.09932 16.9366 7.11691 17.019 7.15108C17.1013 7.18525 17.1761 7.23533 17.2391 7.29845ZM14.4231 13.2042L18.3792 9.24893L16.746 7.61541L12.7899 11.5713L14.4231 13.2042ZM17.4555 0.415771H16.7768V3.13037H17.4555V0.415771ZM17.4555 15.3462H16.7768V18.0608H17.4555V15.3462Z" fill="#ff6700" class="svelte-82ixrs"></path></svg>', r = te(), a = B("div"), H && H.c(), u = te(), p && p.c(), g(t, "data-testid", "textbox"), g(t, "class", wt(
        /*show_magic*/
        l[15] ? "scroll_hide_magic" : "scroll-hide"
      ) + " svelte-82ixrs"), g(t, "dir", n = /*rtl*/
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
      l[12] : ""), g(f, "class", "extend_button svelte-82ixrs"), g(f, "aria-label", "Extend"), g(f, "aria-roledescription", "Extend text"), g(e, "class", "magic_container svelte-82ixrs"), g(a, "class", "menu svelte-82ixrs");
    },
    m(v, m) {
      ee(v, e, m), F(e, t), ze(
        t,
        /*value*/
        l[0]
      ), l[32](t), F(e, i), F(e, f), ee(v, r, m), ee(v, a, m), H && H.m(a, null), F(a, u), p && p.m(a, null), c = !0, /*autofocus*/
      l[11] && t.focus(), h || (L = [
        bt(o = /*text_area_resize*/
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
          f,
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
      v[12] : "")) && g(t, "style", s), o && gt(o.update) && m[0] & /*value*/
      1 && o.update.call(
        null,
        /*value*/
        v[0]
      ), m[0] & /*value*/
      1 && ze(
        t,
        /*value*/
        v[0]
      ), /*prompts*/
      v[8].length > 0 ? H ? H.p(v, m) : (H = jt(v), H.c(), H.m(a, u)) : H && (H.d(1), H = null), /*suffixes*/
      v[9].length > 0 ? p ? p.p(v, m) : (p = Pt(v), p.c(), p.m(a, null)) : p && (p.d(1), p = null);
    },
    i(v) {
      c || (v && oi(() => {
        c && (_ || (_ = Tt(a, Et, {}, !0)), _.run(1));
      }), c = !0);
    },
    o(v) {
      v && (_ || (_ = Tt(a, Et, {}, !1)), _.run(0)), c = !1;
    },
    d(v) {
      v && ($(e), $(r), $(a)), l[32](null), H && H.d(), p && p.d(), v && _ && _.end(), h = !1, vt(L);
    }
  };
}
function jt(l) {
  let e, t, n, s, o = Ue(
    /*prompts*/
    l[8]
  ), i = [];
  for (let f = 0; f < o.length; f += 1)
    i[f] = At(It(l, o, f));
  return {
    c() {
      e = B("div"), t = B("span"), t.textContent = "Best prompt structures", n = te(), s = B("ul");
      for (let f = 0; f < i.length; f += 1)
        i[f].c();
      g(s, "class", "svelte-82ixrs"), g(e, "class", "menu_section svelte-82ixrs");
    },
    m(f, r) {
      ee(f, e, r), F(e, t), F(e, n), F(e, s);
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(s, null);
    },
    p(f, r) {
      if (r[0] & /*addToTextbox, prompts*/
      131328) {
        o = Ue(
          /*prompts*/
          f[8]
        );
        let a;
        for (a = 0; a < o.length; a += 1) {
          const u = It(f, o, a);
          i[a] ? i[a].p(u, r) : (i[a] = At(u), i[a].c(), i[a].m(s, null));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = o.length;
      }
    },
    d(f) {
      f && $(e), kl(i, f);
    }
  };
}
function At(l) {
  let e, t, n = (
    /*word*/
    l[47] + ""
  ), s, o, i, f, r, a, u;
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
      e = B("li"), t = B("button"), s = pt(n), o = te(), i = Ge("svg"), f = Ge("path"), r = te(), g(f, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), g(f, "fill", "#FF9A57"), g(f, "class", "svelte-82ixrs"), g(i, "xmlns", "http://www.w3.org/2000/svg"), g(i, "width", "11"), g(i, "height", "12"), g(i, "viewBox", "0 0 11 12"), g(i, "fill", "none"), g(i, "class", "svelte-82ixrs"), g(t, "class", "text_extension_button_prompt svelte-82ixrs"), g(e, "class", "svelte-82ixrs");
    },
    m(c, h) {
      ee(c, e, h), F(e, t), F(t, s), F(t, o), F(t, i), F(i, f), F(e, r), a || (u = E(t, "click", _), a = !0);
    },
    p(c, h) {
      l = c, h[0] & /*prompts*/
      256 && n !== (n = /*word*/
      l[47] + "") && kt(s, n);
    },
    d(c) {
      c && $(e), a = !1, u();
    }
  };
}
function Pt(l) {
  let e, t, n, s, o = Ue(
    /*suffixes*/
    l[9]
  ), i = [];
  for (let f = 0; f < o.length; f += 1)
    i[f] = Yt(Dt(l, o, f));
  return {
    c() {
      e = B("div"), t = B("span"), t.textContent = "Best style keywords", n = te(), s = B("ul");
      for (let f = 0; f < i.length; f += 1)
        i[f].c();
      g(s, "class", "svelte-82ixrs"), g(e, "class", "menu_section svelte-82ixrs");
    },
    m(f, r) {
      ee(f, e, r), F(e, t), F(e, n), F(e, s);
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(s, null);
    },
    p(f, r) {
      if (r[0] & /*addToTextbox, suffixes*/
      131584) {
        o = Ue(
          /*suffixes*/
          f[9]
        );
        let a;
        for (a = 0; a < o.length; a += 1) {
          const u = Dt(f, o, a);
          i[a] ? i[a].p(u, r) : (i[a] = Yt(u), i[a].c(), i[a].m(s, null));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = o.length;
      }
    },
    d(f) {
      f && $(e), kl(i, f);
    }
  };
}
function Yt(l) {
  let e, t, n = (
    /*word*/
    l[47] + ""
  ), s, o, i, f, r, a, u;
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
      e = B("li"), t = B("button"), s = pt(n), o = te(), i = Ge("svg"), f = Ge("path"), r = te(), g(f, "d", "M8.70801 5.51112H5.95801V2.57779C5.95801 2.44813 5.90972 2.32377 5.82376 2.23209C5.73781 2.14041 5.62123 2.0889 5.49967 2.0889C5.37812 2.0889 5.26154 2.14041 5.17558 2.23209C5.08963 2.32377 5.04134 2.44813 5.04134 2.57779V5.51112H2.29134C2.16978 5.51112 2.0532 5.56263 1.96725 5.65431C1.8813 5.746 1.83301 5.87035 1.83301 6.00001C1.83301 6.12967 1.8813 6.25402 1.96725 6.34571C2.0532 6.43739 2.16978 6.4889 2.29134 6.4889H5.04134V9.42223C5.04134 9.55189 5.08963 9.67624 5.17558 9.76793C5.26154 9.85961 5.37812 9.91112 5.49967 9.91112C5.62123 9.91112 5.73781 9.85961 5.82376 9.76793C5.90972 9.67624 5.95801 9.55189 5.95801 9.42223V6.4889H8.70801C8.82956 6.4889 8.94614 6.43739 9.0321 6.34571C9.11805 6.25402 9.16634 6.12967 9.16634 6.00001C9.16634 5.87035 9.11805 5.746 9.0321 5.65431C8.94614 5.56263 8.82956 5.51112 8.70801 5.51112Z"), g(f, "fill", "#FF9A57"), g(f, "class", "svelte-82ixrs"), g(i, "xmlns", "http://www.w3.org/2000/svg"), g(i, "width", "11"), g(i, "height", "12"), g(i, "viewBox", "0 0 11 12"), g(i, "fill", "none"), g(i, "class", "svelte-82ixrs"), g(t, "class", "text_extension_button svelte-82ixrs"), g(e, "class", "svelte-82ixrs");
    },
    m(c, h) {
      ee(c, e, h), F(e, t), F(t, s), F(t, o), F(t, i), F(i, f), F(e, r), a || (u = E(t, "click", _), a = !0);
    },
    p(c, h) {
      l = c, h[0] & /*suffixes*/
      512 && n !== (n = /*word*/
      l[47] + "") && kt(s, n);
    },
    d(c) {
      c && $(e), a = !1, u();
    }
  };
}
function pi(l) {
  let e, t, n, s, o, i, f;
  t = new Zn({
    props: {
      show_label: (
        /*show_label*/
        l[6]
      ),
      info: (
        /*info*/
        l[4]
      ),
      $$slots: { default: [gi] },
      $$scope: { ctx: l }
    }
  });
  const r = [ki, vi, wi], a = [];
  function u(_, c) {
    return (
      /*show_menu*/
      _[14] && /*show_magic*/
      _[15] ? 0 : !/*show_menu*/
      _[14] && /*show_magic*/
      _[15] ? 1 : 2
    );
  }
  return o = u(l), i = a[o] = r[o](l), {
    c() {
      e = B("label"), ai(t.$$.fragment), n = te(), s = B("div"), i.c(), g(s, "class", "input-container"), g(e, "class", "svelte-82ixrs"), Bt(
        e,
        "container",
        /*container*/
        l[7]
      );
    },
    m(_, c) {
      ee(_, e, c), ci(t, e, null), F(e, n), F(e, s), a[o].m(s, null), f = !0;
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
      let L = o;
      o = u(_), o === L ? a[o].p(_, c) : (ui(), at(a[L], 1, 1, () => {
        a[L] = null;
      }), fi(), i = a[o], i ? i.p(_, c) : (i = a[o] = r[o](_), i.c()), ft(i, 1), i.m(s, null)), (!f || c[0] & /*container*/
      128) && Bt(
        e,
        "container",
        /*container*/
        _[7]
      );
    },
    i(_) {
      f || (ft(t.$$.fragment, _), ft(i), f = !0);
    },
    o(_) {
      at(t.$$.fragment, _), at(i), f = !1;
    },
    d(_) {
      _ && $(e), ri(t), a[o].d();
    }
  };
}
function Ci(l, e, t) {
  var n = this && this.__awaiter || function(d, S, D, A) {
    function me(Te) {
      return Te instanceof D ? Te : new D(function(De) {
        De(Te);
      });
    }
    return new (D || (D = Promise))(function(Te, De) {
      function Fl(he) {
        try {
          lt(A.next(he));
        } catch (nt) {
          De(nt);
        }
      }
      function Zl(he) {
        try {
          lt(A.throw(he));
        } catch (nt) {
          De(nt);
        }
      }
      function lt(he) {
        he.done ? Te(he.value) : me(he.value).then(Fl, Zl);
      }
      lt((A = A.apply(d, S || [])).next());
    });
  };
  let { value: s = "" } = e, { value_is_output: o = !1 } = e, { lines: i = 1 } = e, { placeholder: f = "Type here..." } = e, { label: r } = e, { info: a = void 0 } = e, { disabled: u = !1 } = e, { show_label: _ = !0 } = e, { container: c = !0 } = e, { max_lines: h } = e, { prompts: L = [] } = e, { suffixes: H = [] } = e, { rtl: p = !1 } = e, { autofocus: v = !1 } = e, { text_align: m = void 0 } = e, { autoscroll: b = !0 } = e, C, T = !1, k, N = 0, I = !1, ae = L.length > 0 || H.length > 0;
  const j = bi();
  mi(() => {
    k = C && C.offsetHeight + C.scrollTop > C.scrollHeight - 100;
  });
  const le = () => {
    k && b && !I && C.scrollTo(0, C.scrollHeight);
  };
  function ne() {
    j("change", s), o || j("input");
  }
  hi(() => {
    v && C.focus(), k && b && le(), t(22, o = !1);
  });
  function ge() {
    return n(this, void 0, void 0, function* () {
      t(14, T = !T);
    });
  }
  function Y(d) {
    t(0, s += `${d} `);
  }
  function re(d) {
    const S = d.target, D = S.value, A = [S.selectionStart, S.selectionEnd];
    j("select", { value: D.substring(...A), index: A });
  }
  function O(d) {
    return n(this, void 0, void 0, function* () {
      yield Nt(), (d.key === "Enter" && d.shiftKey && i > 1 || d.key === "Enter" && !d.shiftKey && i === 1 && h >= 1) && (d.preventDefault(), j("submit"));
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
      if (yield Nt(), i === h)
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
  function ke(d) {
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
  function pe(d) {
    ot[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  const Ce = (d) => Y(d), $e = (d) => Y(d);
  function de() {
    s = this.value, t(0, s);
  }
  function ye(d) {
    ot[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  function et() {
    s = this.value, t(0, s);
  }
  function tt(d) {
    ot[d ? "unshift" : "push"](() => {
      C = d, t(13, C);
    });
  }
  return l.$$set = (d) => {
    "value" in d && t(0, s = d.value), "value_is_output" in d && t(22, o = d.value_is_output), "lines" in d && t(1, i = d.lines), "placeholder" in d && t(2, f = d.placeholder), "label" in d && t(3, r = d.label), "info" in d && t(4, a = d.info), "disabled" in d && t(5, u = d.disabled), "show_label" in d && t(6, _ = d.show_label), "container" in d && t(7, c = d.container), "max_lines" in d && t(23, h = d.max_lines), "prompts" in d && t(8, L = d.prompts), "suffixes" in d && t(9, H = d.suffixes), "rtl" in d && t(10, p = d.rtl), "autofocus" in d && t(11, v = d.autofocus), "text_align" in d && t(12, m = d.text_align), "autoscroll" in d && t(24, b = d.autoscroll);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*value*/
    1 && s === null && t(0, s = ""), l.$$.dirty[0] & /*value, el, lines, max_lines*/
    8396803 && C && i !== h && _e({ target: C }), l.$$.dirty[0] & /*value*/
    1 && ne();
  }, [
    s,
    i,
    f,
    r,
    a,
    u,
    _,
    c,
    L,
    H,
    p,
    v,
    m,
    C,
    T,
    ae,
    ge,
    Y,
    re,
    O,
    we,
    ve,
    o,
    h,
    b,
    w,
    ke,
    We,
    Je,
    Qe,
    y,
    xe,
    pe,
    Ce,
    $e,
    de,
    ye,
    et,
    tt
  ];
}
class yi extends si {
  constructor(e) {
    super(), _i(
      this,
      e,
      Ci,
      pi,
      di,
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
  SvelteComponent: Li,
  append: W,
  attr: q,
  component_subscribe: Kt,
  detach: Mi,
  element: Vi,
  init: Hi,
  insert: qi,
  noop: Ot,
  safe_not_equal: Fi,
  set_style: je,
  svg_element: J,
  toggle_class: Ut
} = window.__gradio__svelte__internal, { onMount: Zi } = window.__gradio__svelte__internal;
function Si(l) {
  let e, t, n, s, o, i, f, r, a, u, _, c;
  return {
    c() {
      e = Vi("div"), t = J("svg"), n = J("g"), s = J("path"), o = J("path"), i = J("path"), f = J("path"), r = J("g"), a = J("path"), u = J("path"), _ = J("path"), c = J("path"), q(s, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(s, "fill", "#FF7C00"), q(s, "fill-opacity", "0.4"), q(s, "class", "svelte-43sxxs"), q(o, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(o, "fill", "#FF7C00"), q(o, "class", "svelte-43sxxs"), q(i, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(f, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(f, "fill", "#FF7C00"), q(f, "class", "svelte-43sxxs"), je(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(a, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(a, "fill", "#FF7C00"), q(a, "fill-opacity", "0.4"), q(a, "class", "svelte-43sxxs"), q(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(u, "fill", "#FF7C00"), q(u, "class", "svelte-43sxxs"), q(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(_, "fill", "#FF7C00"), q(_, "fill-opacity", "0.4"), q(_, "class", "svelte-43sxxs"), q(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), je(r, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Ut(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(h, L) {
      qi(h, e, L), W(e, t), W(t, n), W(n, s), W(n, o), W(n, i), W(n, f), W(t, r), W(r, a), W(r, u), W(r, _), W(r, c);
    },
    p(h, [L]) {
      L & /*$top*/
      2 && je(n, "transform", "translate(" + /*$top*/
      h[1][0] + "px, " + /*$top*/
      h[1][1] + "px)"), L & /*$bottom*/
      4 && je(r, "transform", "translate(" + /*$bottom*/
      h[2][0] + "px, " + /*$bottom*/
      h[2][1] + "px)"), L & /*margin*/
      1 && Ut(
        e,
        "margin",
        /*margin*/
        h[0]
      );
    },
    i: Ot,
    o: Ot,
    d(h) {
      h && Mi(e);
    }
  };
}
function zi(l, e, t) {
  let n, s;
  var o = this && this.__awaiter || function(h, L, H, p) {
    function v(m) {
      return m instanceof H ? m : new H(function(b) {
        b(m);
      });
    }
    return new (H || (H = Promise))(function(m, b) {
      function C(N) {
        try {
          k(p.next(N));
        } catch (I) {
          b(I);
        }
      }
      function T(N) {
        try {
          k(p.throw(N));
        } catch (I) {
          b(I);
        }
      }
      function k(N) {
        N.done ? m(N.value) : v(N.value).then(C, T);
      }
      k((p = p.apply(h, L || [])).next());
    });
  };
  let { margin: i = !0 } = e;
  const f = zt([0, 0]);
  Kt(l, f, (h) => t(1, n = h));
  const r = zt([0, 0]);
  Kt(l, r, (h) => t(2, s = h));
  let a;
  function u() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([f.set([125, 140]), r.set([-125, -140])]), yield Promise.all([f.set([-125, 140]), r.set([125, -140])]), yield Promise.all([f.set([-125, 0]), r.set([125, -0])]), yield Promise.all([f.set([125, 0]), r.set([-125, 0])]);
    });
  }
  function _() {
    return o(this, void 0, void 0, function* () {
      yield u(), a || _();
    });
  }
  function c() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([f.set([125, 0]), r.set([-125, 0])]), _();
    });
  }
  return Zi(() => (c(), () => a = !0)), l.$$set = (h) => {
    "margin" in h && t(0, i = h.margin);
  }, [i, n, s, f, r];
}
class Ei extends Li {
  constructor(e) {
    super(), Hi(this, e, zi, Si, Fi, { margin: 0 });
  }
}
const {
  SvelteComponent: Ti,
  append: be,
  attr: x,
  binding_callbacks: Xt,
  check_outros: dt,
  create_component: pl,
  create_slot: Cl,
  destroy_component: yl,
  destroy_each: Ll,
  detach: M,
  element: oe,
  empty: Ee,
  ensure_array_like: Re,
  get_all_dirty_from_scope: Ml,
  get_slot_changes: Vl,
  group_outros: mt,
  init: Bi,
  insert: V,
  mount_component: Hl,
  noop: ht,
  safe_not_equal: Ni,
  set_data: G,
  set_style: ce,
  space: X,
  text: z,
  toggle_class: U,
  transition_in: Q,
  transition_out: fe,
  update_slot_base: ql
} = window.__gradio__svelte__internal, { tick: Di } = window.__gradio__svelte__internal, { onDestroy: Ii } = window.__gradio__svelte__internal, { createEventDispatcher: ji } = window.__gradio__svelte__internal, Ai = (l) => ({}), Gt = (l) => ({}), Pi = (l) => ({}), Rt = (l) => ({});
function Wt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n[43] = t, n;
}
function Jt(l, e, t) {
  const n = l.slice();
  return n[41] = e[t], n;
}
function Yi(l) {
  let e, t, n, s, o = (
    /*i18n*/
    l[1]("common.error") + ""
  ), i, f, r;
  t = new Xn({
    props: {
      Icon: $n,
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
  ), u = Cl(
    a,
    l,
    /*$$scope*/
    l[29],
    Gt
  );
  return {
    c() {
      e = oe("div"), pl(t.$$.fragment), n = X(), s = oe("span"), i = z(o), f = X(), u && u.c(), x(e, "class", "clear-status svelte-vopvsi"), x(s, "class", "error svelte-vopvsi");
    },
    m(_, c) {
      V(_, e, c), Hl(t, e, null), V(_, n, c), V(_, s, c), be(s, i), V(_, f, c), u && u.m(_, c), r = !0;
    },
    p(_, c) {
      const h = {};
      c[0] & /*i18n*/
      2 && (h.label = /*i18n*/
      _[1]("common.clear")), t.$set(h), (!r || c[0] & /*i18n*/
      2) && o !== (o = /*i18n*/
      _[1]("common.error") + "") && G(i, o), u && u.p && (!r || c[0] & /*$$scope*/
      536870912) && ql(
        u,
        a,
        _,
        /*$$scope*/
        _[29],
        r ? Vl(
          a,
          /*$$scope*/
          _[29],
          c,
          Ai
        ) : Ml(
          /*$$scope*/
          _[29]
        ),
        Gt
      );
    },
    i(_) {
      r || (Q(t.$$.fragment, _), Q(u, _), r = !0);
    },
    o(_) {
      fe(t.$$.fragment, _), fe(u, _), r = !1;
    },
    d(_) {
      _ && (M(e), M(n), M(s), M(f)), yl(t), u && u.d(_);
    }
  };
}
function Ki(l) {
  let e, t, n, s, o, i, f, r, a, u = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Qt(l)
  );
  function _(b, C) {
    if (
      /*progress*/
      b[7]
    )
      return Xi;
    if (
      /*queue_position*/
      b[2] !== null && /*queue_size*/
      b[3] !== void 0 && /*queue_position*/
      b[2] >= 0
    )
      return Ui;
    if (
      /*queue_position*/
      b[2] === 0
    )
      return Oi;
  }
  let c = _(l), h = c && c(l), L = (
    /*timer*/
    l[5] && el(l)
  );
  const H = [Ji, Wi], p = [];
  function v(b, C) {
    return (
      /*last_progress_level*/
      b[15] != null ? 0 : (
        /*show_progress*/
        b[6] === "full" ? 1 : -1
      )
    );
  }
  ~(o = v(l)) && (i = p[o] = H[o](l));
  let m = !/*timer*/
  l[5] && fl(l);
  return {
    c() {
      u && u.c(), e = X(), t = oe("div"), h && h.c(), n = X(), L && L.c(), s = X(), i && i.c(), f = X(), m && m.c(), r = Ee(), x(t, "class", "progress-text svelte-vopvsi"), U(
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
      u && u.m(b, C), V(b, e, C), V(b, t, C), h && h.m(t, null), be(t, n), L && L.m(t, null), V(b, s, C), ~o && p[o].m(b, C), V(b, f, C), m && m.m(b, C), V(b, r, C), a = !0;
    },
    p(b, C) {
      /*variant*/
      b[8] === "default" && /*show_eta_bar*/
      b[18] && /*show_progress*/
      b[6] === "full" ? u ? u.p(b, C) : (u = Qt(b), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), c === (c = _(b)) && h ? h.p(b, C) : (h && h.d(1), h = c && c(b), h && (h.c(), h.m(t, n))), /*timer*/
      b[5] ? L ? L.p(b, C) : (L = el(b), L.c(), L.m(t, null)) : L && (L.d(1), L = null), (!a || C[0] & /*variant*/
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
      let T = o;
      o = v(b), o === T ? ~o && p[o].p(b, C) : (i && (mt(), fe(p[T], 1, 1, () => {
        p[T] = null;
      }), dt()), ~o ? (i = p[o], i ? i.p(b, C) : (i = p[o] = H[o](b), i.c()), Q(i, 1), i.m(f.parentNode, f)) : i = null), /*timer*/
      b[5] ? m && (mt(), fe(m, 1, 1, () => {
        m = null;
      }), dt()) : m ? (m.p(b, C), C[0] & /*timer*/
      32 && Q(m, 1)) : (m = fl(b), m.c(), Q(m, 1), m.m(r.parentNode, r));
    },
    i(b) {
      a || (Q(i), Q(m), a = !0);
    },
    o(b) {
      fe(i), fe(m), a = !1;
    },
    d(b) {
      b && (M(e), M(t), M(s), M(f), M(r)), u && u.d(b), h && h.d(), L && L.d(), ~o && p[o].d(b), m && m.d(b);
    }
  };
}
function Qt(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = oe("div"), x(e, "class", "eta-bar svelte-vopvsi"), ce(e, "transform", t);
    },
    m(n, s) {
      V(n, e, s);
    },
    p(n, s) {
      s[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && ce(e, "transform", t);
    },
    d(n) {
      n && M(e);
    }
  };
}
function Oi(l) {
  let e;
  return {
    c() {
      e = z("processing |");
    },
    m(t, n) {
      V(t, e, n);
    },
    p: ht,
    d(t) {
      t && M(e);
    }
  };
}
function Ui(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, s, o, i;
  return {
    c() {
      e = z("queue: "), n = z(t), s = z("/"), o = z(
        /*queue_size*/
        l[3]
      ), i = z(" |");
    },
    m(f, r) {
      V(f, e, r), V(f, n, r), V(f, s, r), V(f, o, r), V(f, i, r);
    },
    p(f, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      f[2] + 1 + "") && G(n, t), r[0] & /*queue_size*/
      8 && G(
        o,
        /*queue_size*/
        f[3]
      );
    },
    d(f) {
      f && (M(e), M(n), M(s), M(o), M(i));
    }
  };
}
function Xi(l) {
  let e, t = Re(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = $t(Jt(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Ee();
    },
    m(s, o) {
      for (let i = 0; i < n.length; i += 1)
        n[i] && n[i].m(s, o);
      V(s, e, o);
    },
    p(s, o) {
      if (o[0] & /*progress*/
      128) {
        t = Re(
          /*progress*/
          s[7]
        );
        let i;
        for (i = 0; i < t.length; i += 1) {
          const f = Jt(s, t, i);
          n[i] ? n[i].p(f, o) : (n[i] = $t(f), n[i].c(), n[i].m(e.parentNode, e));
        }
        for (; i < n.length; i += 1)
          n[i].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && M(e), Ll(n, s);
    }
  };
}
function xt(l) {
  let e, t = (
    /*p*/
    l[41].unit + ""
  ), n, s, o = " ", i;
  function f(u, _) {
    return (
      /*p*/
      u[41].length != null ? Ri : Gi
    );
  }
  let r = f(l), a = r(l);
  return {
    c() {
      a.c(), e = X(), n = z(t), s = z(" | "), i = z(o);
    },
    m(u, _) {
      a.m(u, _), V(u, e, _), V(u, n, _), V(u, s, _), V(u, i, _);
    },
    p(u, _) {
      r === (r = f(u)) && a ? a.p(u, _) : (a.d(1), a = r(u), a && (a.c(), a.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && G(n, t);
    },
    d(u) {
      u && (M(e), M(n), M(s), M(i)), a.d(u);
    }
  };
}
function Gi(l) {
  let e = Fe(
    /*p*/
    l[41].index || 0
  ) + "", t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      V(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = Fe(
        /*p*/
        n[41].index || 0
      ) + "") && G(t, e);
    },
    d(n) {
      n && M(t);
    }
  };
}
function Ri(l) {
  let e = Fe(
    /*p*/
    l[41].index || 0
  ) + "", t, n, s = Fe(
    /*p*/
    l[41].length
  ) + "", o;
  return {
    c() {
      t = z(e), n = z("/"), o = z(s);
    },
    m(i, f) {
      V(i, t, f), V(i, n, f), V(i, o, f);
    },
    p(i, f) {
      f[0] & /*progress*/
      128 && e !== (e = Fe(
        /*p*/
        i[41].index || 0
      ) + "") && G(t, e), f[0] & /*progress*/
      128 && s !== (s = Fe(
        /*p*/
        i[41].length
      ) + "") && G(o, s);
    },
    d(i) {
      i && (M(t), M(n), M(o));
    }
  };
}
function $t(l) {
  let e, t = (
    /*p*/
    l[41].index != null && xt(l)
  );
  return {
    c() {
      t && t.c(), e = Ee();
    },
    m(n, s) {
      t && t.m(n, s), V(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].index != null ? t ? t.p(n, s) : (t = xt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && M(e), t && t.d(n);
    }
  };
}
function el(l) {
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
    m(o, i) {
      V(o, e, i), V(o, n, i), V(o, s, i);
    },
    p(o, i) {
      i[0] & /*formatted_timer*/
      1048576 && G(
        e,
        /*formatted_timer*/
        o[20]
      ), i[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      o[0] ? `/${/*formatted_eta*/
      o[19]}` : "") && G(n, t);
    },
    d(o) {
      o && (M(e), M(n), M(s));
    }
  };
}
function Wi(l) {
  let e, t;
  return e = new Ei({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      pl(e.$$.fragment);
    },
    m(n, s) {
      Hl(e, n, s), t = !0;
    },
    p(n, s) {
      const o = {};
      s[0] & /*variant*/
      256 && (o.margin = /*variant*/
      n[8] === "default"), e.$set(o);
    },
    i(n) {
      t || (Q(e.$$.fragment, n), t = !0);
    },
    o(n) {
      fe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      yl(e, n);
    }
  };
}
function Ji(l) {
  let e, t, n, s, o, i = `${/*last_progress_level*/
  l[15] * 100}%`, f = (
    /*progress*/
    l[7] != null && tl(l)
  );
  return {
    c() {
      e = oe("div"), t = oe("div"), f && f.c(), n = X(), s = oe("div"), o = oe("div"), x(t, "class", "progress-level-inner svelte-vopvsi"), x(o, "class", "progress-bar svelte-vopvsi"), ce(o, "width", i), x(s, "class", "progress-bar-wrap svelte-vopvsi"), x(e, "class", "progress-level svelte-vopvsi");
    },
    m(r, a) {
      V(r, e, a), be(e, t), f && f.m(t, null), be(e, n), be(e, s), be(s, o), l[31](o);
    },
    p(r, a) {
      /*progress*/
      r[7] != null ? f ? f.p(r, a) : (f = tl(r), f.c(), f.m(t, null)) : f && (f.d(1), f = null), a[0] & /*last_progress_level*/
      32768 && i !== (i = `${/*last_progress_level*/
      r[15] * 100}%`) && ce(o, "width", i);
    },
    i: ht,
    o: ht,
    d(r) {
      r && M(e), f && f.d(), l[31](null);
    }
  };
}
function tl(l) {
  let e, t = Re(
    /*progress*/
    l[7]
  ), n = [];
  for (let s = 0; s < t.length; s += 1)
    n[s] = ol(Wt(l, t, s));
  return {
    c() {
      for (let s = 0; s < n.length; s += 1)
        n[s].c();
      e = Ee();
    },
    m(s, o) {
      for (let i = 0; i < n.length; i += 1)
        n[i] && n[i].m(s, o);
      V(s, e, o);
    },
    p(s, o) {
      if (o[0] & /*progress_level, progress*/
      16512) {
        t = Re(
          /*progress*/
          s[7]
        );
        let i;
        for (i = 0; i < t.length; i += 1) {
          const f = Wt(s, t, i);
          n[i] ? n[i].p(f, o) : (n[i] = ol(f), n[i].c(), n[i].m(e.parentNode, e));
        }
        for (; i < n.length; i += 1)
          n[i].d(1);
        n.length = t.length;
      }
    },
    d(s) {
      s && M(e), Ll(n, s);
    }
  };
}
function ll(l) {
  let e, t, n, s, o = (
    /*i*/
    l[43] !== 0 && Qi()
  ), i = (
    /*p*/
    l[41].desc != null && nl(l)
  ), f = (
    /*p*/
    l[41].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null && il()
  ), r = (
    /*progress_level*/
    l[14] != null && sl(l)
  );
  return {
    c() {
      o && o.c(), e = X(), i && i.c(), t = X(), f && f.c(), n = X(), r && r.c(), s = Ee();
    },
    m(a, u) {
      o && o.m(a, u), V(a, e, u), i && i.m(a, u), V(a, t, u), f && f.m(a, u), V(a, n, u), r && r.m(a, u), V(a, s, u);
    },
    p(a, u) {
      /*p*/
      a[41].desc != null ? i ? i.p(a, u) : (i = nl(a), i.c(), i.m(t.parentNode, t)) : i && (i.d(1), i = null), /*p*/
      a[41].desc != null && /*progress_level*/
      a[14] && /*progress_level*/
      a[14][
        /*i*/
        a[43]
      ] != null ? f || (f = il(), f.c(), f.m(n.parentNode, n)) : f && (f.d(1), f = null), /*progress_level*/
      a[14] != null ? r ? r.p(a, u) : (r = sl(a), r.c(), r.m(s.parentNode, s)) : r && (r.d(1), r = null);
    },
    d(a) {
      a && (M(e), M(t), M(n), M(s)), o && o.d(a), i && i.d(a), f && f.d(a), r && r.d(a);
    }
  };
}
function Qi(l) {
  let e;
  return {
    c() {
      e = z(" /");
    },
    m(t, n) {
      V(t, e, n);
    },
    d(t) {
      t && M(e);
    }
  };
}
function nl(l) {
  let e = (
    /*p*/
    l[41].desc + ""
  ), t;
  return {
    c() {
      t = z(e);
    },
    m(n, s) {
      V(n, t, s);
    },
    p(n, s) {
      s[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && G(t, e);
    },
    d(n) {
      n && M(t);
    }
  };
}
function il(l) {
  let e;
  return {
    c() {
      e = z("-");
    },
    m(t, n) {
      V(t, e, n);
    },
    d(t) {
      t && M(e);
    }
  };
}
function sl(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[43]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = z(e), n = z("%");
    },
    m(s, o) {
      V(s, t, o), V(s, n, o);
    },
    p(s, o) {
      o[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (s[14][
        /*i*/
        s[43]
      ] || 0)).toFixed(1) + "") && G(t, e);
    },
    d(s) {
      s && (M(t), M(n));
    }
  };
}
function ol(l) {
  let e, t = (
    /*p*/
    (l[41].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[43]
    ] != null) && ll(l)
  );
  return {
    c() {
      t && t.c(), e = Ee();
    },
    m(n, s) {
      t && t.m(n, s), V(n, e, s);
    },
    p(n, s) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? t ? t.p(n, s) : (t = ll(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && M(e), t && t.d(n);
    }
  };
}
function fl(l) {
  let e, t, n, s;
  const o = (
    /*#slots*/
    l[30]["additional-loading-text"]
  ), i = Cl(
    o,
    l,
    /*$$scope*/
    l[29],
    Rt
  );
  return {
    c() {
      e = oe("p"), t = z(
        /*loading_text*/
        l[9]
      ), n = X(), i && i.c(), x(e, "class", "loading svelte-vopvsi");
    },
    m(f, r) {
      V(f, e, r), be(e, t), V(f, n, r), i && i.m(f, r), s = !0;
    },
    p(f, r) {
      (!s || r[0] & /*loading_text*/
      512) && G(
        t,
        /*loading_text*/
        f[9]
      ), i && i.p && (!s || r[0] & /*$$scope*/
      536870912) && ql(
        i,
        o,
        f,
        /*$$scope*/
        f[29],
        s ? Vl(
          o,
          /*$$scope*/
          f[29],
          r,
          Pi
        ) : Ml(
          /*$$scope*/
          f[29]
        ),
        Rt
      );
    },
    i(f) {
      s || (Q(i, f), s = !0);
    },
    o(f) {
      fe(i, f), s = !1;
    },
    d(f) {
      f && (M(e), M(n)), i && i.d(f);
    }
  };
}
function xi(l) {
  let e, t, n, s, o;
  const i = [Ki, Yi], f = [];
  function r(a, u) {
    return (
      /*status*/
      a[4] === "pending" ? 0 : (
        /*status*/
        a[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(l)) && (n = f[t] = i[t](l)), {
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
    m(a, u) {
      V(a, e, u), ~t && f[t].m(e, null), l[33](e), o = !0;
    },
    p(a, u) {
      let _ = t;
      t = r(a), t === _ ? ~t && f[t].p(a, u) : (n && (mt(), fe(f[_], 1, 1, () => {
        f[_] = null;
      }), dt()), ~t ? (n = f[t], n ? n.p(a, u) : (n = f[t] = i[t](a), n.c()), Q(n, 1), n.m(e, null)) : n = null), (!o || u[0] & /*variant, show_progress*/
      320 && s !== (s = "wrap " + /*variant*/
      a[8] + " " + /*show_progress*/
      a[6] + " svelte-vopvsi")) && x(e, "class", s), (!o || u[0] & /*variant, show_progress, status, show_progress*/
      336) && U(e, "hide", !/*status*/
      a[4] || /*status*/
      a[4] === "complete" || /*show_progress*/
      a[6] === "hidden"), (!o || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && U(
        e,
        "translucent",
        /*variant*/
        a[8] === "center" && /*status*/
        (a[4] === "pending" || /*status*/
        a[4] === "error") || /*translucent*/
        a[11] || /*show_progress*/
        a[6] === "minimal"
      ), (!o || u[0] & /*variant, show_progress, status*/
      336) && U(
        e,
        "generating",
        /*status*/
        a[4] === "generating"
      ), (!o || u[0] & /*variant, show_progress, border*/
      4416) && U(
        e,
        "border",
        /*border*/
        a[12]
      ), u[0] & /*absolute*/
      1024 && ce(
        e,
        "position",
        /*absolute*/
        a[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && ce(
        e,
        "padding",
        /*absolute*/
        a[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(a) {
      o || (Q(n), o = !0);
    },
    o(a) {
      fe(n), o = !1;
    },
    d(a) {
      a && M(e), ~t && f[t].d(), l[33](null);
    }
  };
}
var $i = function(l, e, t, n) {
  function s(o) {
    return o instanceof t ? o : new t(function(i) {
      i(o);
    });
  }
  return new (t || (t = Promise))(function(o, i) {
    function f(u) {
      try {
        a(n.next(u));
      } catch (_) {
        i(_);
      }
    }
    function r(u) {
      try {
        a(n.throw(u));
      } catch (_) {
        i(_);
      }
    }
    function a(u) {
      u.done ? o(u.value) : s(u.value).then(f, r);
    }
    a((n = n.apply(l, e || [])).next());
  });
};
let Ae = [], rt = !1;
function es(l) {
  return $i(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (Ae.push(e), !rt)
        rt = !0;
      else
        return;
      yield Di(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let s = 0; s < Ae.length; s++) {
          const i = Ae[s].getBoundingClientRect();
          (s === 0 || i.top + window.scrollY <= n[0]) && (n[0] = i.top + window.scrollY, n[1] = s);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), rt = !1, Ae = [];
      });
    }
  });
}
function ts(l, e, t) {
  let n, { $$slots: s = {}, $$scope: o } = e;
  this && this.__awaiter;
  const i = ji();
  let { i18n: f } = e, { eta: r = null } = e, { queue_position: a } = e, { queue_size: u } = e, { status: _ } = e, { scroll_to_output: c = !1 } = e, { timer: h = !0 } = e, { show_progress: L = "full" } = e, { message: H = null } = e, { progress: p = null } = e, { variant: v = "default" } = e, { loading_text: m = "Loading..." } = e, { absolute: b = !0 } = e, { translucent: C = !1 } = e, { border: T = !1 } = e, { autoscroll: k } = e, N, I = !1, ae = 0, j = 0, le = null, ne = null, ge = 0, Y = null, re, O = null, we = !0;
  const _e = () => {
    t(0, r = t(27, le = t(19, ke = null))), t(25, ae = performance.now()), t(26, j = 0), I = !0, ve();
  };
  function ve() {
    requestAnimationFrame(() => {
      t(26, j = (performance.now() - ae) / 1e3), I && ve();
    });
  }
  function w() {
    t(26, j = 0), t(0, r = t(27, le = t(19, ke = null))), I && (I = !1);
  }
  Ii(() => {
    I && w();
  });
  let ke = null;
  function We(y) {
    Xt[y ? "unshift" : "push"](() => {
      O = y, t(16, O), t(7, p), t(14, Y), t(15, re);
    });
  }
  const Je = () => {
    i("clear_status");
  };
  function Qe(y) {
    Xt[y ? "unshift" : "push"](() => {
      N = y, t(13, N);
    });
  }
  return l.$$set = (y) => {
    "i18n" in y && t(1, f = y.i18n), "eta" in y && t(0, r = y.eta), "queue_position" in y && t(2, a = y.queue_position), "queue_size" in y && t(3, u = y.queue_size), "status" in y && t(4, _ = y.status), "scroll_to_output" in y && t(22, c = y.scroll_to_output), "timer" in y && t(5, h = y.timer), "show_progress" in y && t(6, L = y.show_progress), "message" in y && t(23, H = y.message), "progress" in y && t(7, p = y.progress), "variant" in y && t(8, v = y.variant), "loading_text" in y && t(9, m = y.loading_text), "absolute" in y && t(10, b = y.absolute), "translucent" in y && t(11, C = y.translucent), "border" in y && t(12, T = y.border), "autoscroll" in y && t(24, k = y.autoscroll), "$$scope" in y && t(29, o = y.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (r === null && t(0, r = le), r != null && le !== r && (t(28, ne = (performance.now() - ae) / 1e3 + r), t(19, ke = ne.toFixed(1)), t(27, le = r))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, ge = ne === null || ne <= 0 || !j ? null : Math.min(j / ne, 1)), l.$$.dirty[0] & /*progress*/
    128 && p != null && t(18, we = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (p != null ? t(14, Y = p.map((y) => {
      if (y.index != null && y.length != null)
        return y.index / y.length;
      if (y.progress != null)
        return y.progress;
    })) : t(14, Y = null), Y ? (t(15, re = Y[Y.length - 1]), O && (re === 0 ? t(16, O.style.transition = "0", O) : t(16, O.style.transition = "150ms", O))) : t(15, re = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? _e() : w()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && N && c && (_ === "pending" || _ === "complete") && es(N, k), l.$$.dirty[0] & /*status, message*/
    8388624, l.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, n = j.toFixed(1));
  }, [
    r,
    f,
    a,
    u,
    _,
    h,
    L,
    p,
    v,
    m,
    b,
    C,
    T,
    N,
    Y,
    re,
    O,
    ge,
    we,
    ke,
    n,
    i,
    c,
    H,
    k,
    ae,
    j,
    le,
    ne,
    o,
    s,
    We,
    Je,
    Qe
  ];
}
class ls extends Ti {
  constructor(e) {
    super(), Bi(
      this,
      e,
      ts,
      xi,
      Ni,
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
  SvelteComponent: ns,
  add_iframe_resize_listener: is,
  add_render_callback: ss,
  append: os,
  attr: fs,
  binding_callbacks: as,
  detach: rs,
  element: us,
  init: _s,
  insert: cs,
  noop: al,
  safe_not_equal: ds,
  set_data: ms,
  text: hs,
  toggle_class: qe
} = window.__gradio__svelte__internal, { onMount: bs } = window.__gradio__svelte__internal;
function gs(l) {
  let e, t = (
    /*value*/
    (l[0] ? (
      /*value*/
      l[0]
    ) : "") + ""
  ), n, s;
  return {
    c() {
      e = us("div"), n = hs(t), fs(e, "class", "svelte-84cxb8"), ss(() => (
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
    m(o, i) {
      cs(o, e, i), os(e, n), s = is(
        e,
        /*div_elementresize_handler*/
        l[5].bind(e)
      ), l[6](e);
    },
    p(o, [i]) {
      i & /*value*/
      1 && t !== (t = /*value*/
      (o[0] ? (
        /*value*/
        o[0]
      ) : "") + "") && ms(n, t), i & /*type*/
      2 && qe(
        e,
        "table",
        /*type*/
        o[1] === "table"
      ), i & /*type*/
      2 && qe(
        e,
        "gallery",
        /*type*/
        o[1] === "gallery"
      ), i & /*selected*/
      4 && qe(
        e,
        "selected",
        /*selected*/
        o[2]
      );
    },
    i: al,
    o: al,
    d(o) {
      o && rs(e), s(), l[6](null);
    }
  };
}
function ws(l, e, t) {
  let { value: n } = e, { type: s } = e, { selected: o = !1 } = e, i, f;
  function r(_, c) {
    !_ || !c || (f.style.setProperty("--local-text-width", `${c < 150 ? c : 200}px`), t(4, f.style.whiteSpace = "unset", f));
  }
  bs(() => {
    r(f, i);
  });
  function a() {
    i = this.clientWidth, t(3, i);
  }
  function u(_) {
    as[_ ? "unshift" : "push"](() => {
      f = _, t(4, f);
    });
  }
  return l.$$set = (_) => {
    "value" in _ && t(0, n = _.value), "type" in _ && t(1, s = _.type), "selected" in _ && t(2, o = _.selected);
  }, [n, s, o, i, f, a, u];
}
class Es extends ns {
  constructor(e) {
    super(), _s(this, e, ws, gs, ds, { value: 0, type: 1, selected: 2 });
  }
}
const {
  SvelteComponent: vs,
  add_flush_callback: rl,
  assign: ks,
  bind: ul,
  binding_callbacks: _l,
  check_outros: ps,
  create_component: Ct,
  destroy_component: yt,
  detach: Cs,
  flush: Z,
  get_spread_object: ys,
  get_spread_update: Ls,
  group_outros: Ms,
  init: Vs,
  insert: Hs,
  mount_component: Lt,
  safe_not_equal: qs,
  space: Fs,
  transition_in: Ze,
  transition_out: Ne
} = window.__gradio__svelte__internal;
function cl(l) {
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
  for (let o = 0; o < n.length; o += 1)
    s = ks(s, n[o]);
  return e = new ls({ props: s }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    l[24]
  ), {
    c() {
      Ct(e.$$.fragment);
    },
    m(o, i) {
      Lt(e, o, i), t = !0;
    },
    p(o, i) {
      const f = i[0] & /*gradio, loading_status*/
      262148 ? Ls(n, [
        i[0] & /*gradio*/
        4 && { autoscroll: (
          /*gradio*/
          o[2].autoscroll
        ) },
        i[0] & /*gradio*/
        4 && { i18n: (
          /*gradio*/
          o[2].i18n
        ) },
        i[0] & /*loading_status*/
        262144 && ys(
          /*loading_status*/
          o[18]
        )
      ]) : {};
      e.$set(f);
    },
    i(o) {
      t || (Ze(e.$$.fragment, o), t = !0);
    },
    o(o) {
      Ne(e.$$.fragment, o), t = !1;
    },
    d(o) {
      yt(e, o);
    }
  };
}
function Zs(l) {
  let e, t, n, s, o, i = (
    /*loading_status*/
    l[18] && cl(l)
  );
  function f(u) {
    l[25](u);
  }
  function r(u) {
    l[26](u);
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
    l[1]), t = new yi({ props: a }), _l.push(() => ul(t, "value", f)), _l.push(() => ul(t, "value_is_output", r)), t.$on(
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
        i && i.c(), e = Fs(), Ct(t.$$.fragment);
      },
      m(u, _) {
        i && i.m(u, _), Hs(u, e, _), Lt(t, u, _), o = !0;
      },
      p(u, _) {
        /*loading_status*/
        u[18] ? i ? (i.p(u, _), _[0] & /*loading_status*/
        262144 && Ze(i, 1)) : (i = cl(u), i.c(), Ze(i, 1), i.m(e.parentNode, e)) : i && (Ms(), Ne(i, 1, 1, () => {
          i = null;
        }), ps());
        const c = {};
        _[0] & /*label*/
        8 && (c.label = /*label*/
        u[3]), _[0] & /*info*/
        16 && (c.info = /*info*/
        u[4]), _[0] & /*show_label*/
        1024 && (c.show_label = /*show_label*/
        u[10]), _[0] & /*lines*/
        256 && (c.lines = /*lines*/
        u[8]), _[0] & /*type*/
        16384 && (c.type = /*type*/
        u[14]), _[0] & /*rtl*/
        524288 && (c.rtl = /*rtl*/
        u[19]), _[0] & /*text_align*/
        1048576 && (c.text_align = /*text_align*/
        u[20]), _[0] & /*max_lines, lines*/
        2304 && (c.max_lines = /*max_lines*/
        u[11] ? (
          /*max_lines*/
          u[11]
        ) : (
          /*lines*/
          u[8] + 1
        )), _[0] & /*prompts*/
        4096 && (c.prompts = /*prompts*/
        u[12]), _[0] & /*suffixes*/
        8192 && (c.suffixes = /*suffixes*/
        u[13]), _[0] & /*placeholder*/
        512 && (c.placeholder = /*placeholder*/
        u[9]), _[0] & /*autofocus*/
        2097152 && (c.autofocus = /*autofocus*/
        u[21]), _[0] & /*container*/
        32768 && (c.container = /*container*/
        u[15]), _[0] & /*autoscroll*/
        4194304 && (c.autoscroll = /*autoscroll*/
        u[22]), _[0] & /*interactive*/
        8388608 && (c.disabled = !/*interactive*/
        u[23]), !n && _[0] & /*value*/
        1 && (n = !0, c.value = /*value*/
        u[0], rl(() => n = !1)), !s && _[0] & /*value_is_output*/
        2 && (s = !0, c.value_is_output = /*value_is_output*/
        u[1], rl(() => s = !1)), t.$set(c);
      },
      i(u) {
        o || (Ze(i), Ze(t.$$.fragment, u), o = !0);
      },
      o(u) {
        Ne(i), Ne(t.$$.fragment, u), o = !1;
      },
      d(u) {
        u && Cs(e), i && i.d(u), yt(t, u);
      }
    }
  );
}
function Ss(l) {
  let e, t;
  return e = new Xl({
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
      $$slots: { default: [Zs] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Ct(e.$$.fragment);
    },
    m(n, s) {
      Lt(e, n, s), t = !0;
    },
    p(n, s) {
      const o = {};
      s[0] & /*visible*/
      128 && (o.visible = /*visible*/
      n[7]), s[0] & /*elem_id*/
      32 && (o.elem_id = /*elem_id*/
      n[5]), s[0] & /*elem_classes*/
      64 && (o.elem_classes = /*elem_classes*/
      n[6]), s[0] & /*scale*/
      65536 && (o.scale = /*scale*/
      n[16]), s[0] & /*min_width*/
      131072 && (o.min_width = /*min_width*/
      n[17]), s[0] & /*container*/
      32768 && (o.padding = /*container*/
      n[15]), s[0] & /*label, info, show_label, lines, type, rtl, text_align, max_lines, prompts, suffixes, placeholder, autofocus, container, autoscroll, interactive, value, value_is_output, gradio, loading_status*/
      16580383 | s[1] & /*$$scope*/
      4 && (o.$$scope = { dirty: s, ctx: n }), e.$set(o);
    },
    i(n) {
      t || (Ze(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Ne(e.$$.fragment, n), t = !1;
    },
    d(n) {
      yt(e, n);
    }
  };
}
function zs(l, e, t) {
  let { gradio: n } = e, { label: s = "Textbox" } = e, { info: o = void 0 } = e, { elem_id: i = "" } = e, { elem_classes: f = [] } = e, { visible: r = !0 } = e, { value: a = "" } = e, { lines: u } = e, { placeholder: _ = "" } = e, { show_label: c } = e, { max_lines: h } = e, { prompts: L = [] } = e, { suffixes: H = [] } = e, { type: p = "text" } = e, { container: v = !0 } = e, { scale: m = null } = e, { min_width: b = void 0 } = e, { loading_status: C = void 0 } = e, { value_is_output: T = !1 } = e, { rtl: k = !1 } = e, { text_align: N = void 0 } = e, { autofocus: I = !1 } = e, { autoscroll: ae = !0 } = e, { interactive: j } = e;
  const le = () => n.dispatch("clear_status", C);
  function ne(w) {
    a = w, t(0, a);
  }
  function ge(w) {
    T = w, t(1, T);
  }
  const Y = () => n.dispatch("change", a), re = () => n.dispatch("input"), O = () => n.dispatch("submit"), we = () => n.dispatch("blur"), _e = (w) => n.dispatch("select", w.detail), ve = () => n.dispatch("focus");
  return l.$$set = (w) => {
    "gradio" in w && t(2, n = w.gradio), "label" in w && t(3, s = w.label), "info" in w && t(4, o = w.info), "elem_id" in w && t(5, i = w.elem_id), "elem_classes" in w && t(6, f = w.elem_classes), "visible" in w && t(7, r = w.visible), "value" in w && t(0, a = w.value), "lines" in w && t(8, u = w.lines), "placeholder" in w && t(9, _ = w.placeholder), "show_label" in w && t(10, c = w.show_label), "max_lines" in w && t(11, h = w.max_lines), "prompts" in w && t(12, L = w.prompts), "suffixes" in w && t(13, H = w.suffixes), "type" in w && t(14, p = w.type), "container" in w && t(15, v = w.container), "scale" in w && t(16, m = w.scale), "min_width" in w && t(17, b = w.min_width), "loading_status" in w && t(18, C = w.loading_status), "value_is_output" in w && t(1, T = w.value_is_output), "rtl" in w && t(19, k = w.rtl), "text_align" in w && t(20, N = w.text_align), "autofocus" in w && t(21, I = w.autofocus), "autoscroll" in w && t(22, ae = w.autoscroll), "interactive" in w && t(23, j = w.interactive);
  }, [
    a,
    T,
    n,
    s,
    o,
    i,
    f,
    r,
    u,
    _,
    c,
    h,
    L,
    H,
    p,
    v,
    m,
    b,
    C,
    k,
    N,
    I,
    ae,
    j,
    le,
    ne,
    ge,
    Y,
    re,
    O,
    we,
    _e,
    ve
  ];
}
class Ts extends vs {
  constructor(e) {
    super(), Vs(
      this,
      e,
      zs,
      Ss,
      qs,
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
  Es as BaseExample,
  yi as BaseTextbox,
  Ts as default
};
