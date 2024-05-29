const {
  SvelteComponent: jn,
  assign: Ln,
  create_slot: Fn,
  detach: Mn,
  element: An,
  get_all_dirty_from_scope: En,
  get_slot_changes: In,
  get_spread_update: Vn,
  init: Bn,
  insert: Dn,
  safe_not_equal: Nn,
  set_dynamic_element_data: Kl,
  set_style: Y,
  toggle_class: me,
  transition_in: Ut,
  transition_out: Wt,
  update_slot_base: Zn
} = window.__gradio__svelte__internal;
function Tn(t) {
  let e, l, n;
  const i = (
    /*#slots*/
    t[18].default
  ), o = Fn(
    i,
    t,
    /*$$scope*/
    t[17],
    null
  );
  let a = [
    { "data-testid": (
      /*test_id*/
      t[7]
    ) },
    { id: (
      /*elem_id*/
      t[2]
    ) },
    {
      class: l = "block " + /*elem_classes*/
      t[3].join(" ") + " svelte-nl1om8"
    }
  ], r = {};
  for (let f = 0; f < a.length; f += 1)
    r = Ln(r, a[f]);
  return {
    c() {
      e = An(
        /*tag*/
        t[14]
      ), o && o.c(), Kl(
        /*tag*/
        t[14]
      )(e, r), me(
        e,
        "hidden",
        /*visible*/
        t[10] === !1
      ), me(
        e,
        "padded",
        /*padding*/
        t[6]
      ), me(
        e,
        "border_focus",
        /*border_mode*/
        t[5] === "focus"
      ), me(
        e,
        "border_contrast",
        /*border_mode*/
        t[5] === "contrast"
      ), me(e, "hide-container", !/*explicit_call*/
      t[8] && !/*container*/
      t[9]), Y(
        e,
        "height",
        /*get_dimension*/
        t[15](
          /*height*/
          t[0]
        )
      ), Y(e, "width", typeof /*width*/
      t[1] == "number" ? `calc(min(${/*width*/
      t[1]}px, 100%))` : (
        /*get_dimension*/
        t[15](
          /*width*/
          t[1]
        )
      )), Y(
        e,
        "border-style",
        /*variant*/
        t[4]
      ), Y(
        e,
        "overflow",
        /*allow_overflow*/
        t[11] ? "visible" : "hidden"
      ), Y(
        e,
        "flex-grow",
        /*scale*/
        t[12]
      ), Y(e, "min-width", `calc(min(${/*min_width*/
      t[13]}px, 100%))`), Y(e, "border-width", "var(--block-border-width)");
    },
    m(f, s) {
      Dn(f, e, s), o && o.m(e, null), n = !0;
    },
    p(f, s) {
      o && o.p && (!n || s & /*$$scope*/
      131072) && Zn(
        o,
        i,
        f,
        /*$$scope*/
        f[17],
        n ? In(
          i,
          /*$$scope*/
          f[17],
          s,
          null
        ) : En(
          /*$$scope*/
          f[17]
        ),
        null
      ), Kl(
        /*tag*/
        f[14]
      )(e, r = Vn(a, [
        (!n || s & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          f[7]
        ) },
        (!n || s & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          f[2]
        ) },
        (!n || s & /*elem_classes*/
        8 && l !== (l = "block " + /*elem_classes*/
        f[3].join(" ") + " svelte-nl1om8")) && { class: l }
      ])), me(
        e,
        "hidden",
        /*visible*/
        f[10] === !1
      ), me(
        e,
        "padded",
        /*padding*/
        f[6]
      ), me(
        e,
        "border_focus",
        /*border_mode*/
        f[5] === "focus"
      ), me(
        e,
        "border_contrast",
        /*border_mode*/
        f[5] === "contrast"
      ), me(e, "hide-container", !/*explicit_call*/
      f[8] && !/*container*/
      f[9]), s & /*height*/
      1 && Y(
        e,
        "height",
        /*get_dimension*/
        f[15](
          /*height*/
          f[0]
        )
      ), s & /*width*/
      2 && Y(e, "width", typeof /*width*/
      f[1] == "number" ? `calc(min(${/*width*/
      f[1]}px, 100%))` : (
        /*get_dimension*/
        f[15](
          /*width*/
          f[1]
        )
      )), s & /*variant*/
      16 && Y(
        e,
        "border-style",
        /*variant*/
        f[4]
      ), s & /*allow_overflow*/
      2048 && Y(
        e,
        "overflow",
        /*allow_overflow*/
        f[11] ? "visible" : "hidden"
      ), s & /*scale*/
      4096 && Y(
        e,
        "flex-grow",
        /*scale*/
        f[12]
      ), s & /*min_width*/
      8192 && Y(e, "min-width", `calc(min(${/*min_width*/
      f[13]}px, 100%))`);
    },
    i(f) {
      n || (Ut(o, f), n = !0);
    },
    o(f) {
      Wt(o, f), n = !1;
    },
    d(f) {
      f && Mn(e), o && o.d(f);
    }
  };
}
function Pn(t) {
  let e, l = (
    /*tag*/
    t[14] && Tn(t)
  );
  return {
    c() {
      l && l.c();
    },
    m(n, i) {
      l && l.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && l.p(n, i);
    },
    i(n) {
      e || (Ut(l, n), e = !0);
    },
    o(n) {
      Wt(l, n), e = !1;
    },
    d(n) {
      l && l.d(n);
    }
  };
}
function Rn(t, e, l) {
  let { $$slots: n = {}, $$scope: i } = e, { height: o = void 0 } = e, { width: a = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: f = [] } = e, { variant: s = "solid" } = e, { border_mode: _ = "base" } = e, { padding: u = !0 } = e, { type: d = "normal" } = e, { test_id: b = void 0 } = e, { explicit_call: w = !1 } = e, { container: y = !0 } = e, { visible: C = !0 } = e, { allow_overflow: k = !0 } = e, { scale: v = null } = e, { min_width: m = 0 } = e, h = d === "fieldset" ? "fieldset" : "div";
  const q = (p) => {
    if (p !== void 0) {
      if (typeof p == "number")
        return p + "px";
      if (typeof p == "string")
        return p;
    }
  };
  return t.$$set = (p) => {
    "height" in p && l(0, o = p.height), "width" in p && l(1, a = p.width), "elem_id" in p && l(2, r = p.elem_id), "elem_classes" in p && l(3, f = p.elem_classes), "variant" in p && l(4, s = p.variant), "border_mode" in p && l(5, _ = p.border_mode), "padding" in p && l(6, u = p.padding), "type" in p && l(16, d = p.type), "test_id" in p && l(7, b = p.test_id), "explicit_call" in p && l(8, w = p.explicit_call), "container" in p && l(9, y = p.container), "visible" in p && l(10, C = p.visible), "allow_overflow" in p && l(11, k = p.allow_overflow), "scale" in p && l(12, v = p.scale), "min_width" in p && l(13, m = p.min_width), "$$scope" in p && l(17, i = p.$$scope);
  }, [
    o,
    a,
    r,
    f,
    s,
    _,
    u,
    b,
    w,
    y,
    C,
    k,
    v,
    m,
    h,
    q,
    d,
    i,
    n
  ];
}
class On extends jn {
  constructor(e) {
    super(), Bn(this, e, Rn, Pn, Nn, {
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
  SvelteComponent: Gn,
  append: jl,
  attr: fl,
  create_component: Xn,
  destroy_component: Hn,
  detach: Un,
  element: Ql,
  init: Wn,
  insert: Yn,
  mount_component: Jn,
  safe_not_equal: Kn,
  set_data: Qn,
  space: xn,
  text: $n,
  toggle_class: Se,
  transition_in: ei,
  transition_out: li
} = window.__gradio__svelte__internal;
function ti(t) {
  let e, l, n, i, o, a;
  return n = new /*Icon*/
  t[1]({}), {
    c() {
      e = Ql("label"), l = Ql("span"), Xn(n.$$.fragment), i = xn(), o = $n(
        /*label*/
        t[0]
      ), fl(l, "class", "svelte-9gxdi0"), fl(e, "for", ""), fl(e, "data-testid", "block-label"), fl(e, "class", "svelte-9gxdi0"), Se(e, "hide", !/*show_label*/
      t[2]), Se(e, "sr-only", !/*show_label*/
      t[2]), Se(
        e,
        "float",
        /*float*/
        t[4]
      ), Se(
        e,
        "hide-label",
        /*disable*/
        t[3]
      );
    },
    m(r, f) {
      Yn(r, e, f), jl(e, l), Jn(n, l, null), jl(e, i), jl(e, o), a = !0;
    },
    p(r, [f]) {
      (!a || f & /*label*/
      1) && Qn(
        o,
        /*label*/
        r[0]
      ), (!a || f & /*show_label*/
      4) && Se(e, "hide", !/*show_label*/
      r[2]), (!a || f & /*show_label*/
      4) && Se(e, "sr-only", !/*show_label*/
      r[2]), (!a || f & /*float*/
      16) && Se(
        e,
        "float",
        /*float*/
        r[4]
      ), (!a || f & /*disable*/
      8) && Se(
        e,
        "hide-label",
        /*disable*/
        r[3]
      );
    },
    i(r) {
      a || (ei(n.$$.fragment, r), a = !0);
    },
    o(r) {
      li(n.$$.fragment, r), a = !1;
    },
    d(r) {
      r && Un(e), Hn(n);
    }
  };
}
function ni(t, e, l) {
  let { label: n = null } = e, { Icon: i } = e, { show_label: o = !0 } = e, { disable: a = !1 } = e, { float: r = !0 } = e;
  return t.$$set = (f) => {
    "label" in f && l(0, n = f.label), "Icon" in f && l(1, i = f.Icon), "show_label" in f && l(2, o = f.show_label), "disable" in f && l(3, a = f.disable), "float" in f && l(4, r = f.float);
  }, [n, i, o, a, r];
}
class ii extends Gn {
  constructor(e) {
    super(), Wn(this, e, ni, ti, Kn, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: oi,
  append: Zl,
  attr: ve,
  bubble: si,
  create_component: fi,
  destroy_component: ai,
  detach: Yt,
  element: Tl,
  init: ri,
  insert: Jt,
  listen: _i,
  mount_component: ui,
  safe_not_equal: ci,
  set_data: di,
  set_style: Oe,
  space: mi,
  text: bi,
  toggle_class: H,
  transition_in: hi,
  transition_out: gi
} = window.__gradio__svelte__internal;
function xl(t) {
  let e, l;
  return {
    c() {
      e = Tl("span"), l = bi(
        /*label*/
        t[1]
      ), ve(e, "class", "svelte-1lrphxw");
    },
    m(n, i) {
      Jt(n, e, i), Zl(e, l);
    },
    p(n, i) {
      i & /*label*/
      2 && di(
        l,
        /*label*/
        n[1]
      );
    },
    d(n) {
      n && Yt(e);
    }
  };
}
function wi(t) {
  let e, l, n, i, o, a, r, f = (
    /*show_label*/
    t[2] && xl(t)
  );
  return i = new /*Icon*/
  t[0]({}), {
    c() {
      e = Tl("button"), f && f.c(), l = mi(), n = Tl("div"), fi(i.$$.fragment), ve(n, "class", "svelte-1lrphxw"), H(
        n,
        "small",
        /*size*/
        t[4] === "small"
      ), H(
        n,
        "large",
        /*size*/
        t[4] === "large"
      ), H(
        n,
        "medium",
        /*size*/
        t[4] === "medium"
      ), e.disabled = /*disabled*/
      t[7], ve(
        e,
        "aria-label",
        /*label*/
        t[1]
      ), ve(
        e,
        "aria-haspopup",
        /*hasPopup*/
        t[8]
      ), ve(
        e,
        "title",
        /*label*/
        t[1]
      ), ve(e, "class", "svelte-1lrphxw"), H(
        e,
        "pending",
        /*pending*/
        t[3]
      ), H(
        e,
        "padded",
        /*padded*/
        t[5]
      ), H(
        e,
        "highlight",
        /*highlight*/
        t[6]
      ), H(
        e,
        "transparent",
        /*transparent*/
        t[9]
      ), Oe(e, "color", !/*disabled*/
      t[7] && /*_color*/
      t[12] ? (
        /*_color*/
        t[12]
      ) : "var(--block-label-text-color)"), Oe(e, "--bg-color", /*disabled*/
      t[7] ? "auto" : (
        /*background*/
        t[10]
      )), Oe(
        e,
        "margin-left",
        /*offset*/
        t[11] + "px"
      );
    },
    m(s, _) {
      Jt(s, e, _), f && f.m(e, null), Zl(e, l), Zl(e, n), ui(i, n, null), o = !0, a || (r = _i(
        e,
        "click",
        /*click_handler*/
        t[14]
      ), a = !0);
    },
    p(s, [_]) {
      /*show_label*/
      s[2] ? f ? f.p(s, _) : (f = xl(s), f.c(), f.m(e, l)) : f && (f.d(1), f = null), (!o || _ & /*size*/
      16) && H(
        n,
        "small",
        /*size*/
        s[4] === "small"
      ), (!o || _ & /*size*/
      16) && H(
        n,
        "large",
        /*size*/
        s[4] === "large"
      ), (!o || _ & /*size*/
      16) && H(
        n,
        "medium",
        /*size*/
        s[4] === "medium"
      ), (!o || _ & /*disabled*/
      128) && (e.disabled = /*disabled*/
      s[7]), (!o || _ & /*label*/
      2) && ve(
        e,
        "aria-label",
        /*label*/
        s[1]
      ), (!o || _ & /*hasPopup*/
      256) && ve(
        e,
        "aria-haspopup",
        /*hasPopup*/
        s[8]
      ), (!o || _ & /*label*/
      2) && ve(
        e,
        "title",
        /*label*/
        s[1]
      ), (!o || _ & /*pending*/
      8) && H(
        e,
        "pending",
        /*pending*/
        s[3]
      ), (!o || _ & /*padded*/
      32) && H(
        e,
        "padded",
        /*padded*/
        s[5]
      ), (!o || _ & /*highlight*/
      64) && H(
        e,
        "highlight",
        /*highlight*/
        s[6]
      ), (!o || _ & /*transparent*/
      512) && H(
        e,
        "transparent",
        /*transparent*/
        s[9]
      ), _ & /*disabled, _color*/
      4224 && Oe(e, "color", !/*disabled*/
      s[7] && /*_color*/
      s[12] ? (
        /*_color*/
        s[12]
      ) : "var(--block-label-text-color)"), _ & /*disabled, background*/
      1152 && Oe(e, "--bg-color", /*disabled*/
      s[7] ? "auto" : (
        /*background*/
        s[10]
      )), _ & /*offset*/
      2048 && Oe(
        e,
        "margin-left",
        /*offset*/
        s[11] + "px"
      );
    },
    i(s) {
      o || (hi(i.$$.fragment, s), o = !0);
    },
    o(s) {
      gi(i.$$.fragment, s), o = !1;
    },
    d(s) {
      s && Yt(e), f && f.d(), ai(i), a = !1, r();
    }
  };
}
function ki(t, e, l) {
  let n, { Icon: i } = e, { label: o = "" } = e, { show_label: a = !1 } = e, { pending: r = !1 } = e, { size: f = "small" } = e, { padded: s = !0 } = e, { highlight: _ = !1 } = e, { disabled: u = !1 } = e, { hasPopup: d = !1 } = e, { color: b = "var(--block-label-text-color)" } = e, { transparent: w = !1 } = e, { background: y = "var(--background-fill-primary)" } = e, { offset: C = 0 } = e;
  function k(v) {
    si.call(this, t, v);
  }
  return t.$$set = (v) => {
    "Icon" in v && l(0, i = v.Icon), "label" in v && l(1, o = v.label), "show_label" in v && l(2, a = v.show_label), "pending" in v && l(3, r = v.pending), "size" in v && l(4, f = v.size), "padded" in v && l(5, s = v.padded), "highlight" in v && l(6, _ = v.highlight), "disabled" in v && l(7, u = v.disabled), "hasPopup" in v && l(8, d = v.hasPopup), "color" in v && l(13, b = v.color), "transparent" in v && l(9, w = v.transparent), "background" in v && l(10, y = v.background), "offset" in v && l(11, C = v.offset);
  }, t.$$.update = () => {
    t.$$.dirty & /*highlight, color*/
    8256 && l(12, n = _ ? "var(--color-accent)" : b);
  }, [
    i,
    o,
    a,
    r,
    f,
    s,
    _,
    u,
    d,
    w,
    y,
    C,
    n,
    b,
    k
  ];
}
class Xl extends oi {
  constructor(e) {
    super(), ri(this, e, ki, wi, ci, {
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
  SvelteComponent: vi,
  append: pi,
  attr: Ll,
  binding_callbacks: yi,
  create_slot: Ci,
  detach: qi,
  element: $l,
  get_all_dirty_from_scope: Si,
  get_slot_changes: zi,
  init: ji,
  insert: Li,
  safe_not_equal: Fi,
  toggle_class: ze,
  transition_in: Mi,
  transition_out: Ai,
  update_slot_base: Ei
} = window.__gradio__svelte__internal;
function Ii(t) {
  let e, l, n;
  const i = (
    /*#slots*/
    t[5].default
  ), o = Ci(
    i,
    t,
    /*$$scope*/
    t[4],
    null
  );
  return {
    c() {
      e = $l("div"), l = $l("div"), o && o.c(), Ll(l, "class", "icon svelte-3w3rth"), Ll(e, "class", "empty svelte-3w3rth"), Ll(e, "aria-label", "Empty value"), ze(
        e,
        "small",
        /*size*/
        t[0] === "small"
      ), ze(
        e,
        "large",
        /*size*/
        t[0] === "large"
      ), ze(
        e,
        "unpadded_box",
        /*unpadded_box*/
        t[1]
      ), ze(
        e,
        "small_parent",
        /*parent_height*/
        t[3]
      );
    },
    m(a, r) {
      Li(a, e, r), pi(e, l), o && o.m(l, null), t[6](e), n = !0;
    },
    p(a, [r]) {
      o && o.p && (!n || r & /*$$scope*/
      16) && Ei(
        o,
        i,
        a,
        /*$$scope*/
        a[4],
        n ? zi(
          i,
          /*$$scope*/
          a[4],
          r,
          null
        ) : Si(
          /*$$scope*/
          a[4]
        ),
        null
      ), (!n || r & /*size*/
      1) && ze(
        e,
        "small",
        /*size*/
        a[0] === "small"
      ), (!n || r & /*size*/
      1) && ze(
        e,
        "large",
        /*size*/
        a[0] === "large"
      ), (!n || r & /*unpadded_box*/
      2) && ze(
        e,
        "unpadded_box",
        /*unpadded_box*/
        a[1]
      ), (!n || r & /*parent_height*/
      8) && ze(
        e,
        "small_parent",
        /*parent_height*/
        a[3]
      );
    },
    i(a) {
      n || (Mi(o, a), n = !0);
    },
    o(a) {
      Ai(o, a), n = !1;
    },
    d(a) {
      a && qi(e), o && o.d(a), t[6](null);
    }
  };
}
function Vi(t, e, l) {
  let n, { $$slots: i = {}, $$scope: o } = e, { size: a = "small" } = e, { unpadded_box: r = !1 } = e, f;
  function s(u) {
    var d;
    if (!u)
      return !1;
    const { height: b } = u.getBoundingClientRect(), { height: w } = ((d = u.parentElement) === null || d === void 0 ? void 0 : d.getBoundingClientRect()) || { height: b };
    return b > w + 2;
  }
  function _(u) {
    yi[u ? "unshift" : "push"](() => {
      f = u, l(2, f);
    });
  }
  return t.$$set = (u) => {
    "size" in u && l(0, a = u.size), "unpadded_box" in u && l(1, r = u.unpadded_box), "$$scope" in u && l(4, o = u.$$scope);
  }, t.$$.update = () => {
    t.$$.dirty & /*el*/
    4 && l(3, n = s(f));
  }, [a, r, f, n, o, i, _];
}
class Bi extends vi {
  constructor(e) {
    super(), ji(this, e, Vi, Ii, Fi, { size: 0, unpadded_box: 1 });
  }
}
const {
  SvelteComponent: Di,
  append: Fl,
  attr: ne,
  detach: Ni,
  init: Zi,
  insert: Ti,
  noop: Ml,
  safe_not_equal: Pi,
  set_style: be,
  svg_element: al
} = window.__gradio__svelte__internal;
function Ri(t) {
  let e, l, n, i;
  return {
    c() {
      e = al("svg"), l = al("g"), n = al("path"), i = al("path"), ne(n, "d", "M18,6L6.087,17.913"), be(n, "fill", "none"), be(n, "fill-rule", "nonzero"), be(n, "stroke-width", "2px"), ne(l, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), ne(i, "d", "M4.364,4.364L19.636,19.636"), be(i, "fill", "none"), be(i, "fill-rule", "nonzero"), be(i, "stroke-width", "2px"), ne(e, "width", "100%"), ne(e, "height", "100%"), ne(e, "viewBox", "0 0 24 24"), ne(e, "version", "1.1"), ne(e, "xmlns", "http://www.w3.org/2000/svg"), ne(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), ne(e, "xml:space", "preserve"), ne(e, "stroke", "currentColor"), be(e, "fill-rule", "evenodd"), be(e, "clip-rule", "evenodd"), be(e, "stroke-linecap", "round"), be(e, "stroke-linejoin", "round");
    },
    m(o, a) {
      Ti(o, e, a), Fl(e, l), Fl(l, n), Fl(e, i);
    },
    p: Ml,
    i: Ml,
    o: Ml,
    d(o) {
      o && Ni(e);
    }
  };
}
class Oi extends Di {
  constructor(e) {
    super(), Zi(this, e, null, Ri, Pi, {});
  }
}
const {
  SvelteComponent: Gi,
  append: Xi,
  attr: el,
  detach: Hi,
  init: Ui,
  insert: Wi,
  noop: Al,
  safe_not_equal: Yi,
  svg_element: et
} = window.__gradio__svelte__internal;
function Ji(t) {
  let e, l;
  return {
    c() {
      e = et("svg"), l = et("path"), el(l, "d", "M23,20a5,5,0,0,0-3.89,1.89L11.8,17.32a4.46,4.46,0,0,0,0-2.64l7.31-4.57A5,5,0,1,0,18,7a4.79,4.79,0,0,0,.2,1.32l-7.31,4.57a5,5,0,1,0,0,6.22l7.31,4.57A4.79,4.79,0,0,0,18,25a5,5,0,1,0,5-5ZM23,4a3,3,0,1,1-3,3A3,3,0,0,1,23,4ZM7,19a3,3,0,1,1,3-3A3,3,0,0,1,7,19Zm16,9a3,3,0,1,1,3-3A3,3,0,0,1,23,28Z"), el(l, "fill", "currentColor"), el(e, "id", "icon"), el(e, "xmlns", "http://www.w3.org/2000/svg"), el(e, "viewBox", "0 0 32 32");
    },
    m(n, i) {
      Wi(n, e, i), Xi(e, l);
    },
    p: Al,
    i: Al,
    o: Al,
    d(n) {
      n && Hi(e);
    }
  };
}
class Ki extends Gi {
  constructor(e) {
    super(), Ui(this, e, null, Ji, Yi, {});
  }
}
const {
  SvelteComponent: Qi,
  append: El,
  attr: D,
  detach: xi,
  init: $i,
  insert: eo,
  noop: Il,
  safe_not_equal: lo,
  svg_element: rl
} = window.__gradio__svelte__internal;
function to(t) {
  let e, l, n, i;
  return {
    c() {
      e = rl("svg"), l = rl("rect"), n = rl("circle"), i = rl("polyline"), D(l, "x", "3"), D(l, "y", "3"), D(l, "width", "18"), D(l, "height", "18"), D(l, "rx", "2"), D(l, "ry", "2"), D(n, "cx", "8.5"), D(n, "cy", "8.5"), D(n, "r", "1.5"), D(i, "points", "21 15 16 10 5 21"), D(e, "xmlns", "http://www.w3.org/2000/svg"), D(e, "width", "100%"), D(e, "height", "100%"), D(e, "viewBox", "0 0 24 24"), D(e, "fill", "none"), D(e, "stroke", "currentColor"), D(e, "stroke-width", "1.5"), D(e, "stroke-linecap", "round"), D(e, "stroke-linejoin", "round"), D(e, "class", "feather feather-image");
    },
    m(o, a) {
      eo(o, e, a), El(e, l), El(e, n), El(e, i);
    },
    p: Il,
    i: Il,
    o: Il,
    d(o) {
      o && xi(e);
    }
  };
}
let Kt = class extends Qi {
  constructor(e) {
    super(), $i(this, e, null, to, lo, {});
  }
};
const {
  SvelteComponent: no,
  append: lt,
  attr: R,
  detach: io,
  init: oo,
  insert: so,
  noop: tt,
  safe_not_equal: fo,
  svg_element: Vl
} = window.__gradio__svelte__internal;
function ao(t) {
  let e, l, n, i;
  return {
    c() {
      e = Vl("svg"), l = Vl("path"), n = Vl("path"), R(l, "stroke", "currentColor"), R(l, "stroke-width", "1.5"), R(l, "stroke-linecap", "round"), R(l, "d", "M16.472 20H4.1a.6.6 0 0 1-.6-.6V9.6a.6.6 0 0 1 .6-.6h2.768a2 2 0 0 0 1.715-.971l2.71-4.517a1.631 1.631 0 0 1 2.961 1.308l-1.022 3.408a.6.6 0 0 0 .574.772h4.575a2 2 0 0 1 1.93 2.526l-1.91 7A2 2 0 0 1 16.473 20Z"), R(n, "stroke", "currentColor"), R(n, "stroke-width", "1.5"), R(n, "stroke-linecap", "round"), R(n, "stroke-linejoin", "round"), R(n, "d", "M7 20V9"), R(e, "xmlns", "http://www.w3.org/2000/svg"), R(e, "viewBox", "0 0 24 24"), R(e, "fill", i = /*selected*/
      t[0] ? "currentColor" : "none"), R(e, "stroke-width", "1.5"), R(e, "color", "currentColor");
    },
    m(o, a) {
      so(o, e, a), lt(e, l), lt(e, n);
    },
    p(o, [a]) {
      a & /*selected*/
      1 && i !== (i = /*selected*/
      o[0] ? "currentColor" : "none") && R(e, "fill", i);
    },
    i: tt,
    o: tt,
    d(o) {
      o && io(e);
    }
  };
}
function ro(t, e, l) {
  let { selected: n } = e;
  return t.$$set = (i) => {
    "selected" in i && l(0, n = i.selected);
  }, [n];
}
class _o extends no {
  constructor(e) {
    super(), oo(this, e, ro, ao, fo, { selected: 0 });
  }
}
const uo = [
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
], nt = {
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
uo.reduce(
  (t, { color: e, primary: l, secondary: n }) => ({
    ...t,
    [e]: {
      primary: nt[e][l],
      secondary: nt[e][n]
    }
  }),
  {}
);
class co extends Error {
  constructor(e) {
    super(e), this.name = "ShareError";
  }
}
const {
  SvelteComponent: mo,
  create_component: bo,
  destroy_component: ho,
  init: go,
  mount_component: wo,
  safe_not_equal: ko,
  transition_in: vo,
  transition_out: po
} = window.__gradio__svelte__internal, { createEventDispatcher: yo } = window.__gradio__svelte__internal;
function Co(t) {
  let e, l;
  return e = new Xl({
    props: {
      Icon: Ki,
      label: (
        /*i18n*/
        t[2]("common.share")
      ),
      pending: (
        /*pending*/
        t[3]
      )
    }
  }), e.$on(
    "click",
    /*click_handler*/
    t[5]
  ), {
    c() {
      bo(e.$$.fragment);
    },
    m(n, i) {
      wo(e, n, i), l = !0;
    },
    p(n, [i]) {
      const o = {};
      i & /*i18n*/
      4 && (o.label = /*i18n*/
      n[2]("common.share")), i & /*pending*/
      8 && (o.pending = /*pending*/
      n[3]), e.$set(o);
    },
    i(n) {
      l || (vo(e.$$.fragment, n), l = !0);
    },
    o(n) {
      po(e.$$.fragment, n), l = !1;
    },
    d(n) {
      ho(e, n);
    }
  };
}
function qo(t, e, l) {
  const n = yo();
  let { formatter: i } = e, { value: o } = e, { i18n: a } = e, r = !1;
  const f = async () => {
    try {
      l(3, r = !0);
      const s = await i(o);
      n("share", { description: s });
    } catch (s) {
      console.error(s);
      let _ = s instanceof co ? s.message : "Share failed.";
      n("error", _);
    } finally {
      l(3, r = !1);
    }
  };
  return t.$$set = (s) => {
    "formatter" in s && l(0, i = s.formatter), "value" in s && l(1, o = s.value), "i18n" in s && l(2, a = s.i18n);
  }, [i, o, a, r, n, f];
}
class So extends mo {
  constructor(e) {
    super(), go(this, e, qo, Co, ko, { formatter: 0, value: 1, i18n: 2 });
  }
}
function Xe(t) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], l = 0;
  for (; t > 1e3 && l < e.length - 1; )
    t /= 1e3, l++;
  let n = e[l];
  return (Number.isInteger(t) ? t : t.toFixed(1)) + n;
}
function cl() {
}
function zo(t, e) {
  return t != t ? e == e : t !== e || t && typeof t == "object" || typeof t == "function";
}
const Qt = typeof window < "u";
let it = Qt ? () => window.performance.now() : () => Date.now(), xt = Qt ? (t) => requestAnimationFrame(t) : cl;
const We = /* @__PURE__ */ new Set();
function $t(t) {
  We.forEach((e) => {
    e.c(t) || (We.delete(e), e.f());
  }), We.size !== 0 && xt($t);
}
function jo(t) {
  let e;
  return We.size === 0 && xt($t), {
    promise: new Promise((l) => {
      We.add(e = { c: t, f: l });
    }),
    abort() {
      We.delete(e);
    }
  };
}
const Ge = [];
function Lo(t, e = cl) {
  let l;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (zo(t, r) && (t = r, l)) {
      const f = !Ge.length;
      for (const s of n)
        s[1](), Ge.push(s, t);
      if (f) {
        for (let s = 0; s < Ge.length; s += 2)
          Ge[s][0](Ge[s + 1]);
        Ge.length = 0;
      }
    }
  }
  function o(r) {
    i(r(t));
  }
  function a(r, f = cl) {
    const s = [r, f];
    return n.add(s), n.size === 1 && (l = e(i, o) || cl), r(t), () => {
      n.delete(s), n.size === 0 && l && (l(), l = null);
    };
  }
  return { set: i, update: o, subscribe: a };
}
function ot(t) {
  return Object.prototype.toString.call(t) === "[object Date]";
}
function Pl(t, e, l, n) {
  if (typeof l == "number" || ot(l)) {
    const i = n - l, o = (l - e) / (t.dt || 1 / 60), a = t.opts.stiffness * i, r = t.opts.damping * o, f = (a - r) * t.inv_mass, s = (o + f) * t.dt;
    return Math.abs(s) < t.opts.precision && Math.abs(i) < t.opts.precision ? n : (t.settled = !1, ot(l) ? new Date(l.getTime() + s) : l + s);
  } else {
    if (Array.isArray(l))
      return l.map(
        (i, o) => Pl(t, e[o], l[o], n[o])
      );
    if (typeof l == "object") {
      const i = {};
      for (const o in l)
        i[o] = Pl(t, e[o], l[o], n[o]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof l} values`);
  }
}
function st(t, e = {}) {
  const l = Lo(t), { stiffness: n = 0.15, damping: i = 0.8, precision: o = 0.01 } = e;
  let a, r, f, s = t, _ = t, u = 1, d = 0, b = !1;
  function w(C, k = {}) {
    _ = C;
    const v = f = {};
    return t == null || k.hard || y.stiffness >= 1 && y.damping >= 1 ? (b = !0, a = it(), s = C, l.set(t = _), Promise.resolve()) : (k.soft && (d = 1 / ((k.soft === !0 ? 0.5 : +k.soft) * 60), u = 0), r || (a = it(), b = !1, r = jo((m) => {
      if (b)
        return b = !1, r = null, !1;
      u = Math.min(u + d, 1);
      const h = {
        inv_mass: u,
        opts: y,
        settled: !0,
        dt: (m - a) * 60 / 1e3
      }, q = Pl(h, s, t, _);
      return a = m, s = t, l.set(t = q), h.settled && (r = null), !h.settled;
    })), new Promise((m) => {
      r.promise.then(() => {
        v === f && m();
      });
    }));
  }
  const y = {
    set: w,
    update: (C, k) => w(C(_, t), k),
    subscribe: l.subscribe,
    stiffness: n,
    damping: i,
    precision: o
  };
  return y;
}
const {
  SvelteComponent: Fo,
  append: ie,
  attr: M,
  component_subscribe: ft,
  detach: Mo,
  element: Ao,
  init: Eo,
  insert: Io,
  noop: at,
  safe_not_equal: Vo,
  set_style: _l,
  svg_element: oe,
  toggle_class: rt
} = window.__gradio__svelte__internal, { onMount: Bo } = window.__gradio__svelte__internal;
function Do(t) {
  let e, l, n, i, o, a, r, f, s, _, u, d;
  return {
    c() {
      e = Ao("div"), l = oe("svg"), n = oe("g"), i = oe("path"), o = oe("path"), a = oe("path"), r = oe("path"), f = oe("g"), s = oe("path"), _ = oe("path"), u = oe("path"), d = oe("path"), M(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), M(i, "fill", "#FF7C00"), M(i, "fill-opacity", "0.4"), M(i, "class", "svelte-43sxxs"), M(o, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), M(o, "fill", "#FF7C00"), M(o, "class", "svelte-43sxxs"), M(a, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), M(a, "fill", "#FF7C00"), M(a, "fill-opacity", "0.4"), M(a, "class", "svelte-43sxxs"), M(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), M(r, "fill", "#FF7C00"), M(r, "class", "svelte-43sxxs"), _l(n, "transform", "translate(" + /*$top*/
      t[1][0] + "px, " + /*$top*/
      t[1][1] + "px)"), M(s, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), M(s, "fill", "#FF7C00"), M(s, "fill-opacity", "0.4"), M(s, "class", "svelte-43sxxs"), M(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), M(_, "fill", "#FF7C00"), M(_, "class", "svelte-43sxxs"), M(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), M(u, "fill", "#FF7C00"), M(u, "fill-opacity", "0.4"), M(u, "class", "svelte-43sxxs"), M(d, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), M(d, "fill", "#FF7C00"), M(d, "class", "svelte-43sxxs"), _l(f, "transform", "translate(" + /*$bottom*/
      t[2][0] + "px, " + /*$bottom*/
      t[2][1] + "px)"), M(l, "viewBox", "-1200 -1200 3000 3000"), M(l, "fill", "none"), M(l, "xmlns", "http://www.w3.org/2000/svg"), M(l, "class", "svelte-43sxxs"), M(e, "class", "svelte-43sxxs"), rt(
        e,
        "margin",
        /*margin*/
        t[0]
      );
    },
    m(b, w) {
      Io(b, e, w), ie(e, l), ie(l, n), ie(n, i), ie(n, o), ie(n, a), ie(n, r), ie(l, f), ie(f, s), ie(f, _), ie(f, u), ie(f, d);
    },
    p(b, [w]) {
      w & /*$top*/
      2 && _l(n, "transform", "translate(" + /*$top*/
      b[1][0] + "px, " + /*$top*/
      b[1][1] + "px)"), w & /*$bottom*/
      4 && _l(f, "transform", "translate(" + /*$bottom*/
      b[2][0] + "px, " + /*$bottom*/
      b[2][1] + "px)"), w & /*margin*/
      1 && rt(
        e,
        "margin",
        /*margin*/
        b[0]
      );
    },
    i: at,
    o: at,
    d(b) {
      b && Mo(e);
    }
  };
}
function No(t, e, l) {
  let n, i;
  var o = this && this.__awaiter || function(b, w, y, C) {
    function k(v) {
      return v instanceof y ? v : new y(function(m) {
        m(v);
      });
    }
    return new (y || (y = Promise))(function(v, m) {
      function h(L) {
        try {
          p(C.next(L));
        } catch (N) {
          m(N);
        }
      }
      function q(L) {
        try {
          p(C.throw(L));
        } catch (N) {
          m(N);
        }
      }
      function p(L) {
        L.done ? v(L.value) : k(L.value).then(h, q);
      }
      p((C = C.apply(b, w || [])).next());
    });
  };
  let { margin: a = !0 } = e;
  const r = st([0, 0]);
  ft(t, r, (b) => l(1, n = b));
  const f = st([0, 0]);
  ft(t, f, (b) => l(2, i = b));
  let s;
  function _() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 140]), f.set([-125, -140])]), yield Promise.all([r.set([-125, 140]), f.set([125, -140])]), yield Promise.all([r.set([-125, 0]), f.set([125, -0])]), yield Promise.all([r.set([125, 0]), f.set([-125, 0])]);
    });
  }
  function u() {
    return o(this, void 0, void 0, function* () {
      yield _(), s || u();
    });
  }
  function d() {
    return o(this, void 0, void 0, function* () {
      yield Promise.all([r.set([125, 0]), f.set([-125, 0])]), u();
    });
  }
  return Bo(() => (d(), () => s = !0)), t.$$set = (b) => {
    "margin" in b && l(0, a = b.margin);
  }, [a, n, i, r, f];
}
class en extends Fo {
  constructor(e) {
    super(), Eo(this, e, No, Do, Vo, { margin: 0 });
  }
}
const {
  SvelteComponent: Zo,
  append: Be,
  attr: fe,
  binding_callbacks: _t,
  check_outros: Rl,
  create_component: ln,
  create_slot: tn,
  destroy_component: nn,
  destroy_each: on,
  detach: z,
  element: he,
  empty: Ye,
  ensure_array_like: dl,
  get_all_dirty_from_scope: sn,
  get_slot_changes: fn,
  group_outros: Ol,
  init: To,
  insert: j,
  mount_component: an,
  noop: Gl,
  safe_not_equal: Po,
  set_data: $,
  set_style: je,
  space: x,
  text: I,
  toggle_class: K,
  transition_in: se,
  transition_out: ge,
  update_slot_base: rn
} = window.__gradio__svelte__internal, { tick: Ro } = window.__gradio__svelte__internal, { onDestroy: Oo } = window.__gradio__svelte__internal, { createEventDispatcher: Go } = window.__gradio__svelte__internal, Xo = (t) => ({}), ut = (t) => ({}), Ho = (t) => ({}), ct = (t) => ({});
function dt(t, e, l) {
  const n = t.slice();
  return n[41] = e[l], n[43] = l, n;
}
function mt(t, e, l) {
  const n = t.slice();
  return n[41] = e[l], n;
}
function Uo(t) {
  let e, l, n, i, o = (
    /*i18n*/
    t[1]("common.error") + ""
  ), a, r, f;
  l = new Xl({
    props: {
      Icon: Oi,
      label: (
        /*i18n*/
        t[1]("common.clear")
      ),
      disabled: !1
    }
  }), l.$on(
    "click",
    /*click_handler*/
    t[32]
  );
  const s = (
    /*#slots*/
    t[30].error
  ), _ = tn(
    s,
    t,
    /*$$scope*/
    t[29],
    ut
  );
  return {
    c() {
      e = he("div"), ln(l.$$.fragment), n = x(), i = he("span"), a = I(o), r = x(), _ && _.c(), fe(e, "class", "clear-status svelte-vopvsi"), fe(i, "class", "error svelte-vopvsi");
    },
    m(u, d) {
      j(u, e, d), an(l, e, null), j(u, n, d), j(u, i, d), Be(i, a), j(u, r, d), _ && _.m(u, d), f = !0;
    },
    p(u, d) {
      const b = {};
      d[0] & /*i18n*/
      2 && (b.label = /*i18n*/
      u[1]("common.clear")), l.$set(b), (!f || d[0] & /*i18n*/
      2) && o !== (o = /*i18n*/
      u[1]("common.error") + "") && $(a, o), _ && _.p && (!f || d[0] & /*$$scope*/
      536870912) && rn(
        _,
        s,
        u,
        /*$$scope*/
        u[29],
        f ? fn(
          s,
          /*$$scope*/
          u[29],
          d,
          Xo
        ) : sn(
          /*$$scope*/
          u[29]
        ),
        ut
      );
    },
    i(u) {
      f || (se(l.$$.fragment, u), se(_, u), f = !0);
    },
    o(u) {
      ge(l.$$.fragment, u), ge(_, u), f = !1;
    },
    d(u) {
      u && (z(e), z(n), z(i), z(r)), nn(l), _ && _.d(u);
    }
  };
}
function Wo(t) {
  let e, l, n, i, o, a, r, f, s, _ = (
    /*variant*/
    t[8] === "default" && /*show_eta_bar*/
    t[18] && /*show_progress*/
    t[6] === "full" && bt(t)
  );
  function u(m, h) {
    if (
      /*progress*/
      m[7]
    )
      return Ko;
    if (
      /*queue_position*/
      m[2] !== null && /*queue_size*/
      m[3] !== void 0 && /*queue_position*/
      m[2] >= 0
    )
      return Jo;
    if (
      /*queue_position*/
      m[2] === 0
    )
      return Yo;
  }
  let d = u(t), b = d && d(t), w = (
    /*timer*/
    t[5] && wt(t)
  );
  const y = [es, $o], C = [];
  function k(m, h) {
    return (
      /*last_progress_level*/
      m[15] != null ? 0 : (
        /*show_progress*/
        m[6] === "full" ? 1 : -1
      )
    );
  }
  ~(o = k(t)) && (a = C[o] = y[o](t));
  let v = !/*timer*/
  t[5] && St(t);
  return {
    c() {
      _ && _.c(), e = x(), l = he("div"), b && b.c(), n = x(), w && w.c(), i = x(), a && a.c(), r = x(), v && v.c(), f = Ye(), fe(l, "class", "progress-text svelte-vopvsi"), K(
        l,
        "meta-text-center",
        /*variant*/
        t[8] === "center"
      ), K(
        l,
        "meta-text",
        /*variant*/
        t[8] === "default"
      );
    },
    m(m, h) {
      _ && _.m(m, h), j(m, e, h), j(m, l, h), b && b.m(l, null), Be(l, n), w && w.m(l, null), j(m, i, h), ~o && C[o].m(m, h), j(m, r, h), v && v.m(m, h), j(m, f, h), s = !0;
    },
    p(m, h) {
      /*variant*/
      m[8] === "default" && /*show_eta_bar*/
      m[18] && /*show_progress*/
      m[6] === "full" ? _ ? _.p(m, h) : (_ = bt(m), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), d === (d = u(m)) && b ? b.p(m, h) : (b && b.d(1), b = d && d(m), b && (b.c(), b.m(l, n))), /*timer*/
      m[5] ? w ? w.p(m, h) : (w = wt(m), w.c(), w.m(l, null)) : w && (w.d(1), w = null), (!s || h[0] & /*variant*/
      256) && K(
        l,
        "meta-text-center",
        /*variant*/
        m[8] === "center"
      ), (!s || h[0] & /*variant*/
      256) && K(
        l,
        "meta-text",
        /*variant*/
        m[8] === "default"
      );
      let q = o;
      o = k(m), o === q ? ~o && C[o].p(m, h) : (a && (Ol(), ge(C[q], 1, 1, () => {
        C[q] = null;
      }), Rl()), ~o ? (a = C[o], a ? a.p(m, h) : (a = C[o] = y[o](m), a.c()), se(a, 1), a.m(r.parentNode, r)) : a = null), /*timer*/
      m[5] ? v && (Ol(), ge(v, 1, 1, () => {
        v = null;
      }), Rl()) : v ? (v.p(m, h), h[0] & /*timer*/
      32 && se(v, 1)) : (v = St(m), v.c(), se(v, 1), v.m(f.parentNode, f));
    },
    i(m) {
      s || (se(a), se(v), s = !0);
    },
    o(m) {
      ge(a), ge(v), s = !1;
    },
    d(m) {
      m && (z(e), z(l), z(i), z(r), z(f)), _ && _.d(m), b && b.d(), w && w.d(), ~o && C[o].d(m), v && v.d(m);
    }
  };
}
function bt(t) {
  let e, l = `translateX(${/*eta_level*/
  (t[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = he("div"), fe(e, "class", "eta-bar svelte-vopvsi"), je(e, "transform", l);
    },
    m(n, i) {
      j(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && l !== (l = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && je(e, "transform", l);
    },
    d(n) {
      n && z(e);
    }
  };
}
function Yo(t) {
  let e;
  return {
    c() {
      e = I("processing |");
    },
    m(l, n) {
      j(l, e, n);
    },
    p: Gl,
    d(l) {
      l && z(e);
    }
  };
}
function Jo(t) {
  let e, l = (
    /*queue_position*/
    t[2] + 1 + ""
  ), n, i, o, a;
  return {
    c() {
      e = I("queue: "), n = I(l), i = I("/"), o = I(
        /*queue_size*/
        t[3]
      ), a = I(" |");
    },
    m(r, f) {
      j(r, e, f), j(r, n, f), j(r, i, f), j(r, o, f), j(r, a, f);
    },
    p(r, f) {
      f[0] & /*queue_position*/
      4 && l !== (l = /*queue_position*/
      r[2] + 1 + "") && $(n, l), f[0] & /*queue_size*/
      8 && $(
        o,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (z(e), z(n), z(i), z(o), z(a));
    }
  };
}
function Ko(t) {
  let e, l = dl(
    /*progress*/
    t[7]
  ), n = [];
  for (let i = 0; i < l.length; i += 1)
    n[i] = gt(mt(t, l, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Ye();
    },
    m(i, o) {
      for (let a = 0; a < n.length; a += 1)
        n[a] && n[a].m(i, o);
      j(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress*/
      128) {
        l = dl(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < l.length; a += 1) {
          const r = mt(i, l, a);
          n[a] ? n[a].p(r, o) : (n[a] = gt(r), n[a].c(), n[a].m(e.parentNode, e));
        }
        for (; a < n.length; a += 1)
          n[a].d(1);
        n.length = l.length;
      }
    },
    d(i) {
      i && z(e), on(n, i);
    }
  };
}
function ht(t) {
  let e, l = (
    /*p*/
    t[41].unit + ""
  ), n, i, o = " ", a;
  function r(_, u) {
    return (
      /*p*/
      _[41].length != null ? xo : Qo
    );
  }
  let f = r(t), s = f(t);
  return {
    c() {
      s.c(), e = x(), n = I(l), i = I(" | "), a = I(o);
    },
    m(_, u) {
      s.m(_, u), j(_, e, u), j(_, n, u), j(_, i, u), j(_, a, u);
    },
    p(_, u) {
      f === (f = r(_)) && s ? s.p(_, u) : (s.d(1), s = f(_), s && (s.c(), s.m(e.parentNode, e))), u[0] & /*progress*/
      128 && l !== (l = /*p*/
      _[41].unit + "") && $(n, l);
    },
    d(_) {
      _ && (z(e), z(n), z(i), z(a)), s.d(_);
    }
  };
}
function Qo(t) {
  let e = Xe(
    /*p*/
    t[41].index || 0
  ) + "", l;
  return {
    c() {
      l = I(e);
    },
    m(n, i) {
      j(n, l, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = Xe(
        /*p*/
        n[41].index || 0
      ) + "") && $(l, e);
    },
    d(n) {
      n && z(l);
    }
  };
}
function xo(t) {
  let e = Xe(
    /*p*/
    t[41].index || 0
  ) + "", l, n, i = Xe(
    /*p*/
    t[41].length
  ) + "", o;
  return {
    c() {
      l = I(e), n = I("/"), o = I(i);
    },
    m(a, r) {
      j(a, l, r), j(a, n, r), j(a, o, r);
    },
    p(a, r) {
      r[0] & /*progress*/
      128 && e !== (e = Xe(
        /*p*/
        a[41].index || 0
      ) + "") && $(l, e), r[0] & /*progress*/
      128 && i !== (i = Xe(
        /*p*/
        a[41].length
      ) + "") && $(o, i);
    },
    d(a) {
      a && (z(l), z(n), z(o));
    }
  };
}
function gt(t) {
  let e, l = (
    /*p*/
    t[41].index != null && ht(t)
  );
  return {
    c() {
      l && l.c(), e = Ye();
    },
    m(n, i) {
      l && l.m(n, i), j(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].index != null ? l ? l.p(n, i) : (l = ht(n), l.c(), l.m(e.parentNode, e)) : l && (l.d(1), l = null);
    },
    d(n) {
      n && z(e), l && l.d(n);
    }
  };
}
function wt(t) {
  let e, l = (
    /*eta*/
    t[0] ? `/${/*formatted_eta*/
    t[19]}` : ""
  ), n, i;
  return {
    c() {
      e = I(
        /*formatted_timer*/
        t[20]
      ), n = I(l), i = I("s");
    },
    m(o, a) {
      j(o, e, a), j(o, n, a), j(o, i, a);
    },
    p(o, a) {
      a[0] & /*formatted_timer*/
      1048576 && $(
        e,
        /*formatted_timer*/
        o[20]
      ), a[0] & /*eta, formatted_eta*/
      524289 && l !== (l = /*eta*/
      o[0] ? `/${/*formatted_eta*/
      o[19]}` : "") && $(n, l);
    },
    d(o) {
      o && (z(e), z(n), z(i));
    }
  };
}
function $o(t) {
  let e, l;
  return e = new en({
    props: { margin: (
      /*variant*/
      t[8] === "default"
    ) }
  }), {
    c() {
      ln(e.$$.fragment);
    },
    m(n, i) {
      an(e, n, i), l = !0;
    },
    p(n, i) {
      const o = {};
      i[0] & /*variant*/
      256 && (o.margin = /*variant*/
      n[8] === "default"), e.$set(o);
    },
    i(n) {
      l || (se(e.$$.fragment, n), l = !0);
    },
    o(n) {
      ge(e.$$.fragment, n), l = !1;
    },
    d(n) {
      nn(e, n);
    }
  };
}
function es(t) {
  let e, l, n, i, o, a = `${/*last_progress_level*/
  t[15] * 100}%`, r = (
    /*progress*/
    t[7] != null && kt(t)
  );
  return {
    c() {
      e = he("div"), l = he("div"), r && r.c(), n = x(), i = he("div"), o = he("div"), fe(l, "class", "progress-level-inner svelte-vopvsi"), fe(o, "class", "progress-bar svelte-vopvsi"), je(o, "width", a), fe(i, "class", "progress-bar-wrap svelte-vopvsi"), fe(e, "class", "progress-level svelte-vopvsi");
    },
    m(f, s) {
      j(f, e, s), Be(e, l), r && r.m(l, null), Be(e, n), Be(e, i), Be(i, o), t[31](o);
    },
    p(f, s) {
      /*progress*/
      f[7] != null ? r ? r.p(f, s) : (r = kt(f), r.c(), r.m(l, null)) : r && (r.d(1), r = null), s[0] & /*last_progress_level*/
      32768 && a !== (a = `${/*last_progress_level*/
      f[15] * 100}%`) && je(o, "width", a);
    },
    i: Gl,
    o: Gl,
    d(f) {
      f && z(e), r && r.d(), t[31](null);
    }
  };
}
function kt(t) {
  let e, l = dl(
    /*progress*/
    t[7]
  ), n = [];
  for (let i = 0; i < l.length; i += 1)
    n[i] = qt(dt(t, l, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Ye();
    },
    m(i, o) {
      for (let a = 0; a < n.length; a += 1)
        n[a] && n[a].m(i, o);
      j(i, e, o);
    },
    p(i, o) {
      if (o[0] & /*progress_level, progress*/
      16512) {
        l = dl(
          /*progress*/
          i[7]
        );
        let a;
        for (a = 0; a < l.length; a += 1) {
          const r = dt(i, l, a);
          n[a] ? n[a].p(r, o) : (n[a] = qt(r), n[a].c(), n[a].m(e.parentNode, e));
        }
        for (; a < n.length; a += 1)
          n[a].d(1);
        n.length = l.length;
      }
    },
    d(i) {
      i && z(e), on(n, i);
    }
  };
}
function vt(t) {
  let e, l, n, i, o = (
    /*i*/
    t[43] !== 0 && ls()
  ), a = (
    /*p*/
    t[41].desc != null && pt(t)
  ), r = (
    /*p*/
    t[41].desc != null && /*progress_level*/
    t[14] && /*progress_level*/
    t[14][
      /*i*/
      t[43]
    ] != null && yt()
  ), f = (
    /*progress_level*/
    t[14] != null && Ct(t)
  );
  return {
    c() {
      o && o.c(), e = x(), a && a.c(), l = x(), r && r.c(), n = x(), f && f.c(), i = Ye();
    },
    m(s, _) {
      o && o.m(s, _), j(s, e, _), a && a.m(s, _), j(s, l, _), r && r.m(s, _), j(s, n, _), f && f.m(s, _), j(s, i, _);
    },
    p(s, _) {
      /*p*/
      s[41].desc != null ? a ? a.p(s, _) : (a = pt(s), a.c(), a.m(l.parentNode, l)) : a && (a.d(1), a = null), /*p*/
      s[41].desc != null && /*progress_level*/
      s[14] && /*progress_level*/
      s[14][
        /*i*/
        s[43]
      ] != null ? r || (r = yt(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      s[14] != null ? f ? f.p(s, _) : (f = Ct(s), f.c(), f.m(i.parentNode, i)) : f && (f.d(1), f = null);
    },
    d(s) {
      s && (z(e), z(l), z(n), z(i)), o && o.d(s), a && a.d(s), r && r.d(s), f && f.d(s);
    }
  };
}
function ls(t) {
  let e;
  return {
    c() {
      e = I(" /");
    },
    m(l, n) {
      j(l, e, n);
    },
    d(l) {
      l && z(e);
    }
  };
}
function pt(t) {
  let e = (
    /*p*/
    t[41].desc + ""
  ), l;
  return {
    c() {
      l = I(e);
    },
    m(n, i) {
      j(n, l, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[41].desc + "") && $(l, e);
    },
    d(n) {
      n && z(l);
    }
  };
}
function yt(t) {
  let e;
  return {
    c() {
      e = I("-");
    },
    m(l, n) {
      j(l, e, n);
    },
    d(l) {
      l && z(e);
    }
  };
}
function Ct(t) {
  let e = (100 * /*progress_level*/
  (t[14][
    /*i*/
    t[43]
  ] || 0)).toFixed(1) + "", l, n;
  return {
    c() {
      l = I(e), n = I("%");
    },
    m(i, o) {
      j(i, l, o), j(i, n, o);
    },
    p(i, o) {
      o[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && $(l, e);
    },
    d(i) {
      i && (z(l), z(n));
    }
  };
}
function qt(t) {
  let e, l = (
    /*p*/
    (t[41].desc != null || /*progress_level*/
    t[14] && /*progress_level*/
    t[14][
      /*i*/
      t[43]
    ] != null) && vt(t)
  );
  return {
    c() {
      l && l.c(), e = Ye();
    },
    m(n, i) {
      l && l.m(n, i), j(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[41].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[43]
      ] != null ? l ? l.p(n, i) : (l = vt(n), l.c(), l.m(e.parentNode, e)) : l && (l.d(1), l = null);
    },
    d(n) {
      n && z(e), l && l.d(n);
    }
  };
}
function St(t) {
  let e, l, n, i;
  const o = (
    /*#slots*/
    t[30]["additional-loading-text"]
  ), a = tn(
    o,
    t,
    /*$$scope*/
    t[29],
    ct
  );
  return {
    c() {
      e = he("p"), l = I(
        /*loading_text*/
        t[9]
      ), n = x(), a && a.c(), fe(e, "class", "loading svelte-vopvsi");
    },
    m(r, f) {
      j(r, e, f), Be(e, l), j(r, n, f), a && a.m(r, f), i = !0;
    },
    p(r, f) {
      (!i || f[0] & /*loading_text*/
      512) && $(
        l,
        /*loading_text*/
        r[9]
      ), a && a.p && (!i || f[0] & /*$$scope*/
      536870912) && rn(
        a,
        o,
        r,
        /*$$scope*/
        r[29],
        i ? fn(
          o,
          /*$$scope*/
          r[29],
          f,
          Ho
        ) : sn(
          /*$$scope*/
          r[29]
        ),
        ct
      );
    },
    i(r) {
      i || (se(a, r), i = !0);
    },
    o(r) {
      ge(a, r), i = !1;
    },
    d(r) {
      r && (z(e), z(n)), a && a.d(r);
    }
  };
}
function ts(t) {
  let e, l, n, i, o;
  const a = [Wo, Uo], r = [];
  function f(s, _) {
    return (
      /*status*/
      s[4] === "pending" ? 0 : (
        /*status*/
        s[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(l = f(t)) && (n = r[l] = a[l](t)), {
    c() {
      e = he("div"), n && n.c(), fe(e, "class", i = "wrap " + /*variant*/
      t[8] + " " + /*show_progress*/
      t[6] + " svelte-vopvsi"), K(e, "hide", !/*status*/
      t[4] || /*status*/
      t[4] === "complete" || /*show_progress*/
      t[6] === "hidden"), K(
        e,
        "translucent",
        /*variant*/
        t[8] === "center" && /*status*/
        (t[4] === "pending" || /*status*/
        t[4] === "error") || /*translucent*/
        t[11] || /*show_progress*/
        t[6] === "minimal"
      ), K(
        e,
        "generating",
        /*status*/
        t[4] === "generating"
      ), K(
        e,
        "border",
        /*border*/
        t[12]
      ), je(
        e,
        "position",
        /*absolute*/
        t[10] ? "absolute" : "static"
      ), je(
        e,
        "padding",
        /*absolute*/
        t[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(s, _) {
      j(s, e, _), ~l && r[l].m(e, null), t[33](e), o = !0;
    },
    p(s, _) {
      let u = l;
      l = f(s), l === u ? ~l && r[l].p(s, _) : (n && (Ol(), ge(r[u], 1, 1, () => {
        r[u] = null;
      }), Rl()), ~l ? (n = r[l], n ? n.p(s, _) : (n = r[l] = a[l](s), n.c()), se(n, 1), n.m(e, null)) : n = null), (!o || _[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      s[8] + " " + /*show_progress*/
      s[6] + " svelte-vopvsi")) && fe(e, "class", i), (!o || _[0] & /*variant, show_progress, status, show_progress*/
      336) && K(e, "hide", !/*status*/
      s[4] || /*status*/
      s[4] === "complete" || /*show_progress*/
      s[6] === "hidden"), (!o || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && K(
        e,
        "translucent",
        /*variant*/
        s[8] === "center" && /*status*/
        (s[4] === "pending" || /*status*/
        s[4] === "error") || /*translucent*/
        s[11] || /*show_progress*/
        s[6] === "minimal"
      ), (!o || _[0] & /*variant, show_progress, status*/
      336) && K(
        e,
        "generating",
        /*status*/
        s[4] === "generating"
      ), (!o || _[0] & /*variant, show_progress, border*/
      4416) && K(
        e,
        "border",
        /*border*/
        s[12]
      ), _[0] & /*absolute*/
      1024 && je(
        e,
        "position",
        /*absolute*/
        s[10] ? "absolute" : "static"
      ), _[0] & /*absolute*/
      1024 && je(
        e,
        "padding",
        /*absolute*/
        s[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(s) {
      o || (se(n), o = !0);
    },
    o(s) {
      ge(n), o = !1;
    },
    d(s) {
      s && z(e), ~l && r[l].d(), t[33](null);
    }
  };
}
var ns = function(t, e, l, n) {
  function i(o) {
    return o instanceof l ? o : new l(function(a) {
      a(o);
    });
  }
  return new (l || (l = Promise))(function(o, a) {
    function r(_) {
      try {
        s(n.next(_));
      } catch (u) {
        a(u);
      }
    }
    function f(_) {
      try {
        s(n.throw(_));
      } catch (u) {
        a(u);
      }
    }
    function s(_) {
      _.done ? o(_.value) : i(_.value).then(r, f);
    }
    s((n = n.apply(t, e || [])).next());
  });
};
let ul = [], Bl = !1;
function is(t) {
  return ns(this, arguments, void 0, function* (e, l = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && l !== !0)) {
      if (ul.push(e), !Bl)
        Bl = !0;
      else
        return;
      yield Ro(), requestAnimationFrame(() => {
        let n = [0, 0];
        for (let i = 0; i < ul.length; i++) {
          const a = ul[i].getBoundingClientRect();
          (i === 0 || a.top + window.scrollY <= n[0]) && (n[0] = a.top + window.scrollY, n[1] = i);
        }
        window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Bl = !1, ul = [];
      });
    }
  });
}
function os(t, e, l) {
  let n, { $$slots: i = {}, $$scope: o } = e;
  this && this.__awaiter;
  const a = Go();
  let { i18n: r } = e, { eta: f = null } = e, { queue_position: s } = e, { queue_size: _ } = e, { status: u } = e, { scroll_to_output: d = !1 } = e, { timer: b = !0 } = e, { show_progress: w = "full" } = e, { message: y = null } = e, { progress: C = null } = e, { variant: k = "default" } = e, { loading_text: v = "Loading..." } = e, { absolute: m = !0 } = e, { translucent: h = !1 } = e, { border: q = !1 } = e, { autoscroll: p } = e, L, N = !1, _e = 0, W = 0, J = null, S = null, we = 0, Z = null, ee, G = null, qe = !0;
  const le = () => {
    l(0, f = l(27, J = l(19, ce = null))), l(25, _e = performance.now()), l(26, W = 0), N = !0, ue();
  };
  function ue() {
    requestAnimationFrame(() => {
      l(26, W = (performance.now() - _e) / 1e3), N && ue();
    });
  }
  function B() {
    l(26, W = 0), l(0, f = l(27, J = l(19, ce = null))), N && (N = !1);
  }
  Oo(() => {
    N && B();
  });
  let ce = null;
  function Ae(c) {
    _t[c ? "unshift" : "push"](() => {
      G = c, l(16, G), l(7, C), l(14, Z), l(15, ee);
    });
  }
  const Ze = () => {
    a("clear_status");
  };
  function Je(c) {
    _t[c ? "unshift" : "push"](() => {
      L = c, l(13, L);
    });
  }
  return t.$$set = (c) => {
    "i18n" in c && l(1, r = c.i18n), "eta" in c && l(0, f = c.eta), "queue_position" in c && l(2, s = c.queue_position), "queue_size" in c && l(3, _ = c.queue_size), "status" in c && l(4, u = c.status), "scroll_to_output" in c && l(22, d = c.scroll_to_output), "timer" in c && l(5, b = c.timer), "show_progress" in c && l(6, w = c.show_progress), "message" in c && l(23, y = c.message), "progress" in c && l(7, C = c.progress), "variant" in c && l(8, k = c.variant), "loading_text" in c && l(9, v = c.loading_text), "absolute" in c && l(10, m = c.absolute), "translucent" in c && l(11, h = c.translucent), "border" in c && l(12, q = c.border), "autoscroll" in c && l(24, p = c.autoscroll), "$$scope" in c && l(29, o = c.$$scope);
  }, t.$$.update = () => {
    t.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (f === null && l(0, f = J), f != null && J !== f && (l(28, S = (performance.now() - _e) / 1e3 + f), l(19, ce = S.toFixed(1)), l(27, J = f))), t.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && l(17, we = S === null || S <= 0 || !W ? null : Math.min(W / S, 1)), t.$$.dirty[0] & /*progress*/
    128 && C != null && l(18, qe = !1), t.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (C != null ? l(14, Z = C.map((c) => {
      if (c.index != null && c.length != null)
        return c.index / c.length;
      if (c.progress != null)
        return c.progress;
    })) : l(14, Z = null), Z ? (l(15, ee = Z[Z.length - 1]), G && (ee === 0 ? l(16, G.style.transition = "0", G) : l(16, G.style.transition = "150ms", G))) : l(15, ee = void 0)), t.$$.dirty[0] & /*status*/
    16 && (u === "pending" ? le() : B()), t.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && L && d && (u === "pending" || u === "complete") && is(L, p), t.$$.dirty[0] & /*status, message*/
    8388624, t.$$.dirty[0] & /*timer_diff*/
    67108864 && l(20, n = W.toFixed(1));
  }, [
    f,
    r,
    s,
    _,
    u,
    b,
    w,
    C,
    k,
    v,
    m,
    h,
    q,
    L,
    Z,
    ee,
    G,
    we,
    qe,
    ce,
    n,
    a,
    d,
    y,
    p,
    _e,
    W,
    J,
    S,
    o,
    i,
    Ae,
    Ze,
    Je
  ];
}
class ss extends Zo {
  constructor(e) {
    super(), To(
      this,
      e,
      os,
      ts,
      Po,
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
  SvelteComponent: fs,
  append: _n,
  attr: E,
  bubble: as,
  check_outros: rs,
  create_slot: un,
  detach: il,
  element: pl,
  empty: _s,
  get_all_dirty_from_scope: cn,
  get_slot_changes: dn,
  group_outros: us,
  init: cs,
  insert: ol,
  listen: ds,
  safe_not_equal: ms,
  set_style: U,
  space: mn,
  src_url_equal: ml,
  toggle_class: He,
  transition_in: bl,
  transition_out: hl,
  update_slot_base: bn
} = window.__gradio__svelte__internal;
function bs(t) {
  let e, l, n, i, o, a, r = (
    /*icon*/
    t[7] && zt(t)
  );
  const f = (
    /*#slots*/
    t[12].default
  ), s = un(
    f,
    t,
    /*$$scope*/
    t[11],
    null
  );
  return {
    c() {
      e = pl("button"), r && r.c(), l = mn(), s && s.c(), E(e, "class", n = /*size*/
      t[4] + " " + /*variant*/
      t[3] + " " + /*elem_classes*/
      t[1].join(" ") + " svelte-8huxfn"), E(
        e,
        "id",
        /*elem_id*/
        t[0]
      ), e.disabled = /*disabled*/
      t[8], He(e, "hidden", !/*visible*/
      t[2]), U(
        e,
        "flex-grow",
        /*scale*/
        t[9]
      ), U(
        e,
        "width",
        /*scale*/
        t[9] === 0 ? "fit-content" : null
      ), U(e, "min-width", typeof /*min_width*/
      t[10] == "number" ? `calc(min(${/*min_width*/
      t[10]}px, 100%))` : null);
    },
    m(_, u) {
      ol(_, e, u), r && r.m(e, null), _n(e, l), s && s.m(e, null), i = !0, o || (a = ds(
        e,
        "click",
        /*click_handler*/
        t[13]
      ), o = !0);
    },
    p(_, u) {
      /*icon*/
      _[7] ? r ? r.p(_, u) : (r = zt(_), r.c(), r.m(e, l)) : r && (r.d(1), r = null), s && s.p && (!i || u & /*$$scope*/
      2048) && bn(
        s,
        f,
        _,
        /*$$scope*/
        _[11],
        i ? dn(
          f,
          /*$$scope*/
          _[11],
          u,
          null
        ) : cn(
          /*$$scope*/
          _[11]
        ),
        null
      ), (!i || u & /*size, variant, elem_classes*/
      26 && n !== (n = /*size*/
      _[4] + " " + /*variant*/
      _[3] + " " + /*elem_classes*/
      _[1].join(" ") + " svelte-8huxfn")) && E(e, "class", n), (!i || u & /*elem_id*/
      1) && E(
        e,
        "id",
        /*elem_id*/
        _[0]
      ), (!i || u & /*disabled*/
      256) && (e.disabled = /*disabled*/
      _[8]), (!i || u & /*size, variant, elem_classes, visible*/
      30) && He(e, "hidden", !/*visible*/
      _[2]), u & /*scale*/
      512 && U(
        e,
        "flex-grow",
        /*scale*/
        _[9]
      ), u & /*scale*/
      512 && U(
        e,
        "width",
        /*scale*/
        _[9] === 0 ? "fit-content" : null
      ), u & /*min_width*/
      1024 && U(e, "min-width", typeof /*min_width*/
      _[10] == "number" ? `calc(min(${/*min_width*/
      _[10]}px, 100%))` : null);
    },
    i(_) {
      i || (bl(s, _), i = !0);
    },
    o(_) {
      hl(s, _), i = !1;
    },
    d(_) {
      _ && il(e), r && r.d(), s && s.d(_), o = !1, a();
    }
  };
}
function hs(t) {
  let e, l, n, i, o = (
    /*icon*/
    t[7] && jt(t)
  );
  const a = (
    /*#slots*/
    t[12].default
  ), r = un(
    a,
    t,
    /*$$scope*/
    t[11],
    null
  );
  return {
    c() {
      e = pl("a"), o && o.c(), l = mn(), r && r.c(), E(
        e,
        "href",
        /*link*/
        t[6]
      ), E(e, "rel", "noopener noreferrer"), E(
        e,
        "aria-disabled",
        /*disabled*/
        t[8]
      ), E(e, "class", n = /*size*/
      t[4] + " " + /*variant*/
      t[3] + " " + /*elem_classes*/
      t[1].join(" ") + " svelte-8huxfn"), E(
        e,
        "id",
        /*elem_id*/
        t[0]
      ), He(e, "hidden", !/*visible*/
      t[2]), He(
        e,
        "disabled",
        /*disabled*/
        t[8]
      ), U(
        e,
        "flex-grow",
        /*scale*/
        t[9]
      ), U(
        e,
        "pointer-events",
        /*disabled*/
        t[8] ? "none" : null
      ), U(
        e,
        "width",
        /*scale*/
        t[9] === 0 ? "fit-content" : null
      ), U(e, "min-width", typeof /*min_width*/
      t[10] == "number" ? `calc(min(${/*min_width*/
      t[10]}px, 100%))` : null);
    },
    m(f, s) {
      ol(f, e, s), o && o.m(e, null), _n(e, l), r && r.m(e, null), i = !0;
    },
    p(f, s) {
      /*icon*/
      f[7] ? o ? o.p(f, s) : (o = jt(f), o.c(), o.m(e, l)) : o && (o.d(1), o = null), r && r.p && (!i || s & /*$$scope*/
      2048) && bn(
        r,
        a,
        f,
        /*$$scope*/
        f[11],
        i ? dn(
          a,
          /*$$scope*/
          f[11],
          s,
          null
        ) : cn(
          /*$$scope*/
          f[11]
        ),
        null
      ), (!i || s & /*link*/
      64) && E(
        e,
        "href",
        /*link*/
        f[6]
      ), (!i || s & /*disabled*/
      256) && E(
        e,
        "aria-disabled",
        /*disabled*/
        f[8]
      ), (!i || s & /*size, variant, elem_classes*/
      26 && n !== (n = /*size*/
      f[4] + " " + /*variant*/
      f[3] + " " + /*elem_classes*/
      f[1].join(" ") + " svelte-8huxfn")) && E(e, "class", n), (!i || s & /*elem_id*/
      1) && E(
        e,
        "id",
        /*elem_id*/
        f[0]
      ), (!i || s & /*size, variant, elem_classes, visible*/
      30) && He(e, "hidden", !/*visible*/
      f[2]), (!i || s & /*size, variant, elem_classes, disabled*/
      282) && He(
        e,
        "disabled",
        /*disabled*/
        f[8]
      ), s & /*scale*/
      512 && U(
        e,
        "flex-grow",
        /*scale*/
        f[9]
      ), s & /*disabled*/
      256 && U(
        e,
        "pointer-events",
        /*disabled*/
        f[8] ? "none" : null
      ), s & /*scale*/
      512 && U(
        e,
        "width",
        /*scale*/
        f[9] === 0 ? "fit-content" : null
      ), s & /*min_width*/
      1024 && U(e, "min-width", typeof /*min_width*/
      f[10] == "number" ? `calc(min(${/*min_width*/
      f[10]}px, 100%))` : null);
    },
    i(f) {
      i || (bl(r, f), i = !0);
    },
    o(f) {
      hl(r, f), i = !1;
    },
    d(f) {
      f && il(e), o && o.d(), r && r.d(f);
    }
  };
}
function zt(t) {
  let e, l, n;
  return {
    c() {
      e = pl("img"), E(e, "class", "button-icon svelte-8huxfn"), ml(e.src, l = /*icon*/
      t[7].url) || E(e, "src", l), E(e, "alt", n = `${/*value*/
      t[5]} icon`);
    },
    m(i, o) {
      ol(i, e, o);
    },
    p(i, o) {
      o & /*icon*/
      128 && !ml(e.src, l = /*icon*/
      i[7].url) && E(e, "src", l), o & /*value*/
      32 && n !== (n = `${/*value*/
      i[5]} icon`) && E(e, "alt", n);
    },
    d(i) {
      i && il(e);
    }
  };
}
function jt(t) {
  let e, l, n;
  return {
    c() {
      e = pl("img"), E(e, "class", "button-icon svelte-8huxfn"), ml(e.src, l = /*icon*/
      t[7].url) || E(e, "src", l), E(e, "alt", n = `${/*value*/
      t[5]} icon`);
    },
    m(i, o) {
      ol(i, e, o);
    },
    p(i, o) {
      o & /*icon*/
      128 && !ml(e.src, l = /*icon*/
      i[7].url) && E(e, "src", l), o & /*value*/
      32 && n !== (n = `${/*value*/
      i[5]} icon`) && E(e, "alt", n);
    },
    d(i) {
      i && il(e);
    }
  };
}
function gs(t) {
  let e, l, n, i;
  const o = [hs, bs], a = [];
  function r(f, s) {
    return (
      /*link*/
      f[6] && /*link*/
      f[6].length > 0 ? 0 : 1
    );
  }
  return e = r(t), l = a[e] = o[e](t), {
    c() {
      l.c(), n = _s();
    },
    m(f, s) {
      a[e].m(f, s), ol(f, n, s), i = !0;
    },
    p(f, [s]) {
      let _ = e;
      e = r(f), e === _ ? a[e].p(f, s) : (us(), hl(a[_], 1, 1, () => {
        a[_] = null;
      }), rs(), l = a[e], l ? l.p(f, s) : (l = a[e] = o[e](f), l.c()), bl(l, 1), l.m(n.parentNode, n));
    },
    i(f) {
      i || (bl(l), i = !0);
    },
    o(f) {
      hl(l), i = !1;
    },
    d(f) {
      f && il(n), a[e].d(f);
    }
  };
}
function ws(t, e, l) {
  let { $$slots: n = {}, $$scope: i } = e, { elem_id: o = "" } = e, { elem_classes: a = [] } = e, { visible: r = !0 } = e, { variant: f = "secondary" } = e, { size: s = "lg" } = e, { value: _ = null } = e, { link: u = null } = e, { icon: d = null } = e, { disabled: b = !1 } = e, { scale: w = null } = e, { min_width: y = void 0 } = e;
  function C(k) {
    as.call(this, t, k);
  }
  return t.$$set = (k) => {
    "elem_id" in k && l(0, o = k.elem_id), "elem_classes" in k && l(1, a = k.elem_classes), "visible" in k && l(2, r = k.visible), "variant" in k && l(3, f = k.variant), "size" in k && l(4, s = k.size), "value" in k && l(5, _ = k.value), "link" in k && l(6, u = k.link), "icon" in k && l(7, d = k.icon), "disabled" in k && l(8, b = k.disabled), "scale" in k && l(9, w = k.scale), "min_width" in k && l(10, y = k.min_width), "$$scope" in k && l(11, i = k.$$scope);
  }, [
    o,
    a,
    r,
    f,
    s,
    _,
    u,
    d,
    b,
    w,
    y,
    i,
    n,
    C
  ];
}
class ks extends fs {
  constructor(e) {
    super(), cs(this, e, ws, gs, ms, {
      elem_id: 0,
      elem_classes: 1,
      visible: 2,
      variant: 3,
      size: 4,
      value: 5,
      link: 6,
      icon: 7,
      disabled: 8,
      scale: 9,
      min_width: 10
    });
  }
}
var Lt = Object.prototype.hasOwnProperty;
function Ft(t, e, l) {
  for (l of t.keys())
    if (ll(l, e))
      return l;
}
function ll(t, e) {
  var l, n, i;
  if (t === e)
    return !0;
  if (t && e && (l = t.constructor) === e.constructor) {
    if (l === Date)
      return t.getTime() === e.getTime();
    if (l === RegExp)
      return t.toString() === e.toString();
    if (l === Array) {
      if ((n = t.length) === e.length)
        for (; n-- && ll(t[n], e[n]); )
          ;
      return n === -1;
    }
    if (l === Set) {
      if (t.size !== e.size)
        return !1;
      for (n of t)
        if (i = n, i && typeof i == "object" && (i = Ft(e, i), !i) || !e.has(i))
          return !1;
      return !0;
    }
    if (l === Map) {
      if (t.size !== e.size)
        return !1;
      for (n of t)
        if (i = n[0], i && typeof i == "object" && (i = Ft(e, i), !i) || !ll(n[1], e.get(i)))
          return !1;
      return !0;
    }
    if (l === ArrayBuffer)
      t = new Uint8Array(t), e = new Uint8Array(e);
    else if (l === DataView) {
      if ((n = t.byteLength) === e.byteLength)
        for (; n-- && t.getInt8(n) === e.getInt8(n); )
          ;
      return n === -1;
    }
    if (ArrayBuffer.isView(t)) {
      if ((n = t.byteLength) === e.byteLength)
        for (; n-- && t[n] === e[n]; )
          ;
      return n === -1;
    }
    if (!l || typeof t == "object") {
      n = 0;
      for (l in t)
        if (Lt.call(t, l) && ++n && !Lt.call(e, l) || !(l in e) || !ll(t[l], e[l]))
          return !1;
      return Object.keys(e).length === n;
    }
  }
  return t !== t && e !== e;
}
const {
  SvelteComponent: vs,
  append: tl,
  attr: pe,
  detach: Hl,
  element: gl,
  flush: Dl,
  init: ps,
  insert: Ul,
  listen: hn,
  noop: Mt,
  safe_not_equal: ys,
  set_data: gn,
  space: At,
  src_url_equal: Et,
  text: wn
} = window.__gradio__svelte__internal, { createEventDispatcher: Cs } = window.__gradio__svelte__internal;
function It(t) {
  let e, l = (
    /*value*/
    t[1].caption + ""
  ), n;
  return {
    c() {
      e = gl("div"), n = wn(l), pe(e, "class", "foot-label left-label svelte-u350v8");
    },
    m(i, o) {
      Ul(i, e, o), tl(e, n);
    },
    p(i, o) {
      o & /*value*/
      2 && l !== (l = /*value*/
      i[1].caption + "") && gn(n, l);
    },
    d(i) {
      i && Hl(e);
    }
  };
}
function Vt(t) {
  let e, l, n, i;
  return {
    c() {
      e = gl("button"), l = wn(
        /*action_label*/
        t[2]
      ), pe(e, "class", "foot-label right-label svelte-u350v8");
    },
    m(o, a) {
      Ul(o, e, a), tl(e, l), n || (i = hn(
        e,
        "click",
        /*click_handler_1*/
        t[5]
      ), n = !0);
    },
    p(o, a) {
      a & /*action_label*/
      4 && gn(
        l,
        /*action_label*/
        o[2]
      );
    },
    d(o) {
      o && Hl(e), n = !1, i();
    }
  };
}
function qs(t) {
  let e, l, n, i, o, a, r, f, s = (
    /*value*/
    t[1].caption && It(t)
  ), _ = (
    /*clickable*/
    t[0] && Vt(t)
  );
  return {
    c() {
      e = gl("div"), l = gl("img"), o = At(), s && s.c(), a = At(), _ && _.c(), pe(l, "alt", n = /*value*/
      t[1].caption || ""), Et(l.src, i = /*value*/
      t[1].image.url) || pe(l, "src", i), pe(l, "class", "thumbnail-img svelte-u350v8"), pe(l, "loading", "lazy"), pe(e, "class", "thumbnail-image-box svelte-u350v8");
    },
    m(u, d) {
      Ul(u, e, d), tl(e, l), tl(e, o), s && s.m(e, null), tl(e, a), _ && _.m(e, null), r || (f = hn(
        l,
        "click",
        /*click_handler*/
        t[4]
      ), r = !0);
    },
    p(u, [d]) {
      d & /*value*/
      2 && n !== (n = /*value*/
      u[1].caption || "") && pe(l, "alt", n), d & /*value*/
      2 && !Et(l.src, i = /*value*/
      u[1].image.url) && pe(l, "src", i), /*value*/
      u[1].caption ? s ? s.p(u, d) : (s = It(u), s.c(), s.m(e, a)) : s && (s.d(1), s = null), /*clickable*/
      u[0] ? _ ? _.p(u, d) : (_ = Vt(u), _.c(), _.m(e, null)) : _ && (_.d(1), _ = null);
    },
    i: Mt,
    o: Mt,
    d(u) {
      u && Hl(e), s && s.d(), _ && _.d(), r = !1, f();
    }
  };
}
function Ss(t, e, l) {
  const n = Cs();
  let { clickable: i } = e, { value: o } = e, { action_label: a } = e;
  const r = () => n("click"), f = () => {
    n("label_click");
  };
  return t.$$set = (s) => {
    "clickable" in s && l(0, i = s.clickable), "value" in s && l(1, o = s.value), "action_label" in s && l(2, a = s.action_label);
  }, [i, o, a, n, r, f];
}
class zs extends vs {
  constructor(e) {
    super(), ps(this, e, Ss, qs, ys, { clickable: 0, value: 1, action_label: 2 });
  }
  get clickable() {
    return this.$$.ctx[0];
  }
  set clickable(e) {
    this.$$set({ clickable: e }), Dl();
  }
  get value() {
    return this.$$.ctx[1];
  }
  set value(e) {
    this.$$set({ value: e }), Dl();
  }
  get action_label() {
    return this.$$.ctx[2];
  }
  set action_label(e) {
    this.$$set({ action_label: e }), Dl();
  }
}
const Nl = [
  {
    key: "xs",
    width: 0
  },
  {
    key: "sm",
    width: 576
  },
  {
    key: "md",
    width: 768
  },
  {
    key: "lg",
    width: 992
  },
  {
    key: "xl",
    width: 1200
  },
  {
    key: "xxl",
    width: 1600
  }
];
async function js(t) {
  if ("clipboard" in navigator)
    await navigator.clipboard.writeText(t);
  else {
    const e = document.createElement("textarea");
    e.value = t, e.style.position = "absolute", e.style.left = "-999999px", document.body.prepend(e), e.select();
    try {
      document.execCommand("copy");
    } catch (l) {
      return Promise.reject(l);
    } finally {
      e.remove();
    }
  }
}
async function Ls(t) {
  return t ? `<div style="display: flex; flex-wrap: wrap; gap: 16px">${(await Promise.all(
    t.map((l) => !l.image || !l.image.url ? "" : l.image.url)
  )).map((l) => `<img src="${l}" style="height: 400px" />`).join("")}</div>` : "";
}
const {
  SvelteComponent: Fs,
  add_iframe_resize_listener: Ms,
  add_render_callback: kn,
  append: P,
  assign: As,
  attr: F,
  binding_callbacks: Bt,
  bubble: Es,
  check_outros: De,
  create_component: Le,
  destroy_component: Fe,
  destroy_each: vn,
  detach: ae,
  element: O,
  empty: Is,
  ensure_array_like: wl,
  get_spread_object: Vs,
  get_spread_update: Bs,
  group_outros: Ne,
  init: Ds,
  insert: re,
  listen: kl,
  mount_component: Me,
  noop: Ns,
  run_all: Zs,
  safe_not_equal: Ts,
  set_data: pn,
  set_style: ye,
  space: Ce,
  src_url_equal: vl,
  text: yn,
  toggle_class: Q,
  transition_in: A,
  transition_out: V
} = window.__gradio__svelte__internal, { createEventDispatcher: Ps, tick: Rs } = window.__gradio__svelte__internal;
function Dt(t, e, l) {
  const n = t.slice();
  return n[54] = e[l], n[56] = l, n;
}
function Nt(t, e, l) {
  const n = t.slice();
  return n[54] = e[l], n[57] = e, n[56] = l, n;
}
function Zt(t) {
  let e, l;
  return e = new ii({
    props: {
      show_label: (
        /*show_label*/
        t[2]
      ),
      Icon: Kt,
      label: (
        /*label*/
        t[4] || "Gallery"
      )
    }
  }), {
    c() {
      Le(e.$$.fragment);
    },
    m(n, i) {
      Me(e, n, i), l = !0;
    },
    p(n, i) {
      const o = {};
      i[0] & /*show_label*/
      4 && (o.show_label = /*show_label*/
      n[2]), i[0] & /*label*/
      16 && (o.label = /*label*/
      n[4] || "Gallery"), e.$set(o);
    },
    i(n) {
      l || (A(e.$$.fragment, n), l = !0);
    },
    o(n) {
      V(e.$$.fragment, n), l = !1;
    },
    d(n) {
      Fe(e, n);
    }
  };
}
function Os(t) {
  let e, l, n, i, o, a, r, f, s, _, u, d = (
    /*selected_image*/
    t[21] && /*allow_preview*/
    t[9] && Tt(t)
  ), b = (
    /*show_share_button*/
    t[10] && Gt(t)
  ), w = wl(
    /*resolved_value*/
    t[16]
  ), y = [];
  for (let h = 0; h < w.length; h += 1)
    y[h] = Xt(Dt(t, w, h));
  const C = (h) => V(y[h], 1, 1, () => {
    y[h] = null;
  }), k = [Hs, Xs], v = [];
  function m(h, q) {
    return (
      /*pending*/
      h[5] ? 0 : 1
    );
  }
  return f = m(t), s = v[f] = k[f](t), {
    c() {
      d && d.c(), e = Ce(), l = O("div"), n = O("div"), b && b.c(), i = Ce(), o = O("div");
      for (let h = 0; h < y.length; h += 1)
        y[h].c();
      a = Ce(), r = O("p"), s.c(), F(n, "class", "grid-container svelte-1p2as1x"), ye(
        n,
        "--object-fit",
        /*object_fit*/
        t[1]
      ), ye(
        n,
        "min-height",
        /*height*/
        t[8] + "px"
      ), Q(
        n,
        "pt-6",
        /*show_label*/
        t[2]
      ), F(r, "class", "loading-line svelte-1p2as1x"), Q(r, "visible", !/*selected_image*/
      (t[21] && /*allow_preview*/
      t[9]) && /*has_more*/
      t[3]), F(l, "class", "grid-wrap svelte-1p2as1x"), ye(
        l,
        "height",
        /*height*/
        t[8] + "px"
      ), kn(() => (
        /*div2_elementresize_handler*/
        t[48].call(l)
      )), Q(l, "fixed-height", !/*height*/
      t[8] || /*height*/
      t[8] === "auto");
    },
    m(h, q) {
      d && d.m(h, q), re(h, e, q), re(h, l, q), P(l, n), b && b.m(n, null), P(n, i), P(n, o);
      for (let p = 0; p < y.length; p += 1)
        y[p] && y[p].m(o, null);
      P(l, a), P(l, r), v[f].m(r, null), _ = Ms(
        l,
        /*div2_elementresize_handler*/
        t[48].bind(l)
      ), u = !0;
    },
    p(h, q) {
      if (/*selected_image*/
      h[21] && /*allow_preview*/
      h[9] ? d ? (d.p(h, q), q[0] & /*selected_image, allow_preview*/
      2097664 && A(d, 1)) : (d = Tt(h), d.c(), A(d, 1), d.m(e.parentNode, e)) : d && (Ne(), V(d, 1, 1, () => {
        d = null;
      }), De()), /*show_share_button*/
      h[10] ? b ? (b.p(h, q), q[0] & /*show_share_button*/
      1024 && A(b, 1)) : (b = Gt(h), b.c(), A(b, 1), b.m(n, i)) : b && (Ne(), V(b, 1, 1, () => {
        b = null;
      }), De()), q[0] & /*resolved_value, selected_index, likeable, clickable, action_label, dispatch*/
      4266049) {
        w = wl(
          /*resolved_value*/
          h[16]
        );
        let L;
        for (L = 0; L < w.length; L += 1) {
          const N = Dt(h, w, L);
          y[L] ? (y[L].p(N, q), A(y[L], 1)) : (y[L] = Xt(N), y[L].c(), A(y[L], 1), y[L].m(o, null));
        }
        for (Ne(), L = w.length; L < y.length; L += 1)
          C(L);
        De();
      }
      (!u || q[0] & /*object_fit*/
      2) && ye(
        n,
        "--object-fit",
        /*object_fit*/
        h[1]
      ), (!u || q[0] & /*height*/
      256) && ye(
        n,
        "min-height",
        /*height*/
        h[8] + "px"
      ), (!u || q[0] & /*show_label*/
      4) && Q(
        n,
        "pt-6",
        /*show_label*/
        h[2]
      );
      let p = f;
      f = m(h), f === p ? v[f].p(h, q) : (Ne(), V(v[p], 1, 1, () => {
        v[p] = null;
      }), De(), s = v[f], s ? s.p(h, q) : (s = v[f] = k[f](h), s.c()), A(s, 1), s.m(r, null)), (!u || q[0] & /*selected_image, allow_preview, has_more*/
      2097672) && Q(r, "visible", !/*selected_image*/
      (h[21] && /*allow_preview*/
      h[9]) && /*has_more*/
      h[3]), (!u || q[0] & /*height*/
      256) && ye(
        l,
        "height",
        /*height*/
        h[8] + "px"
      ), (!u || q[0] & /*height*/
      256) && Q(l, "fixed-height", !/*height*/
      h[8] || /*height*/
      h[8] === "auto");
    },
    i(h) {
      if (!u) {
        A(d), A(b);
        for (let q = 0; q < w.length; q += 1)
          A(y[q]);
        A(s), u = !0;
      }
    },
    o(h) {
      V(d), V(b), y = y.filter(Boolean);
      for (let q = 0; q < y.length; q += 1)
        V(y[q]);
      V(s), u = !1;
    },
    d(h) {
      h && (ae(e), ae(l)), d && d.d(h), b && b.d(), vn(y, h), v[f].d(), _();
    }
  };
}
function Gs(t) {
  let e, l;
  return e = new Bi({
    props: {
      unpadded_box: !0,
      size: "large",
      $$slots: { default: [Ws] },
      $$scope: { ctx: t }
    }
  }), {
    c() {
      Le(e.$$.fragment);
    },
    m(n, i) {
      Me(e, n, i), l = !0;
    },
    p(n, i) {
      const o = {};
      i[1] & /*$$scope*/
      134217728 && (o.$$scope = { dirty: i, ctx: n }), e.$set(o);
    },
    i(n) {
      l || (A(e.$$.fragment, n), l = !0);
    },
    o(n) {
      V(e.$$.fragment, n), l = !1;
    },
    d(n) {
      Fe(e, n);
    }
  };
}
function Tt(t) {
  var v;
  let e, l, n, i, o, a, r, f, s, _, u, d, b, w = (
    /*likeable*/
    t[11] && Pt(t)
  ), y = (
    /*selected_image*/
    ((v = t[21]) == null ? void 0 : v.caption) && Rt(t)
  ), C = wl(
    /*resolved_value*/
    t[16]
  ), k = [];
  for (let m = 0; m < C.length; m += 1)
    k[m] = Ot(Nt(t, C, m));
  return {
    c() {
      e = O("button"), l = O("button"), n = O("img"), r = Ce(), w && w.c(), f = Ce(), y && y.c(), s = Ce(), _ = O("div");
      for (let m = 0; m < k.length; m += 1)
        k[m].c();
      F(n, "data-testid", "detailed-image"), vl(n.src, i = /*selected_image*/
      t[21].image.url) || F(n, "src", i), F(n, "alt", o = /*selected_image*/
      t[21].caption || ""), F(n, "title", a = /*selected_image*/
      t[21].caption || null), F(n, "loading", "lazy"), F(n, "class", "svelte-1p2as1x"), Q(n, "with-caption", !!/*selected_image*/
      t[21].caption), F(l, "class", "image-button svelte-1p2as1x"), ye(l, "height", "calc(100% - " + /*selected_image*/
      (t[21].caption ? "80px" : "60px") + ")"), F(l, "aria-label", "detailed view of selected image"), F(_, "class", "thumbnails scroll-hide svelte-1p2as1x"), F(_, "data-testid", "container_el"), F(e, "class", "preview svelte-1p2as1x");
    },
    m(m, h) {
      re(m, e, h), P(e, l), P(l, n), P(e, r), w && w.m(e, null), P(e, f), y && y.m(e, null), P(e, s), P(e, _);
      for (let q = 0; q < k.length; q += 1)
        k[q] && k[q].m(_, null);
      t[42](_), u = !0, d || (b = [
        kl(
          l,
          "click",
          /*click_handler*/
          t[38]
        ),
        kl(
          e,
          "keydown",
          /*on_keydown*/
          t[24]
        )
      ], d = !0);
    },
    p(m, h) {
      var q;
      if ((!u || h[0] & /*selected_image*/
      2097152 && !vl(n.src, i = /*selected_image*/
      m[21].image.url)) && F(n, "src", i), (!u || h[0] & /*selected_image*/
      2097152 && o !== (o = /*selected_image*/
      m[21].caption || "")) && F(n, "alt", o), (!u || h[0] & /*selected_image*/
      2097152 && a !== (a = /*selected_image*/
      m[21].caption || null)) && F(n, "title", a), (!u || h[0] & /*selected_image*/
      2097152) && Q(n, "with-caption", !!/*selected_image*/
      m[21].caption), (!u || h[0] & /*selected_image*/
      2097152) && ye(l, "height", "calc(100% - " + /*selected_image*/
      (m[21].caption ? "80px" : "60px") + ")"), /*likeable*/
      m[11] ? w ? (w.p(m, h), h[0] & /*likeable*/
      2048 && A(w, 1)) : (w = Pt(m), w.c(), A(w, 1), w.m(e, f)) : w && (Ne(), V(w, 1, 1, () => {
        w = null;
      }), De()), /*selected_image*/
      (q = m[21]) != null && q.caption ? y ? y.p(m, h) : (y = Rt(m), y.c(), y.m(e, s)) : y && (y.d(1), y = null), h[0] & /*resolved_value, el, selected_index*/
      589825) {
        C = wl(
          /*resolved_value*/
          m[16]
        );
        let p;
        for (p = 0; p < C.length; p += 1) {
          const L = Nt(m, C, p);
          k[p] ? k[p].p(L, h) : (k[p] = Ot(L), k[p].c(), k[p].m(_, null));
        }
        for (; p < k.length; p += 1)
          k[p].d(1);
        k.length = C.length;
      }
    },
    i(m) {
      u || (A(w), u = !0);
    },
    o(m) {
      V(w), u = !1;
    },
    d(m) {
      m && ae(e), w && w.d(), y && y.d(), vn(k, m), t[42](null), d = !1, Zs(b);
    }
  };
}
function Pt(t) {
  let e, l, n, i;
  return n = new Xl({
    props: {
      size: "large",
      highlight: (
        /*selected_image*/
        t[21].liked
      ),
      Icon: _o
    }
  }), n.$on(
    "click",
    /*click_handler_1*/
    t[39]
  ), {
    c() {
      e = O("div"), l = O("span"), Le(n.$$.fragment), ye(l, "margin-right", "1px"), F(e, "class", "like-button svelte-1p2as1x");
    },
    m(o, a) {
      re(o, e, a), P(e, l), Me(n, l, null), i = !0;
    },
    p(o, a) {
      const r = {};
      a[0] & /*selected_image*/
      2097152 && (r.highlight = /*selected_image*/
      o[21].liked), n.$set(r);
    },
    i(o) {
      i || (A(n.$$.fragment, o), i = !0);
    },
    o(o) {
      V(n.$$.fragment, o), i = !1;
    },
    d(o) {
      o && ae(e), Fe(n);
    }
  };
}
function Rt(t) {
  let e, l = (
    /*selected_image*/
    t[21].caption + ""
  ), n;
  return {
    c() {
      e = O("caption"), n = yn(l), F(e, "class", "caption svelte-1p2as1x");
    },
    m(i, o) {
      re(i, e, o), P(e, n);
    },
    p(i, o) {
      o[0] & /*selected_image*/
      2097152 && l !== (l = /*selected_image*/
      i[21].caption + "") && pn(n, l);
    },
    d(i) {
      i && ae(e);
    }
  };
}
function Ot(t) {
  let e, l, n, i, o, a, r = (
    /*i*/
    t[56]
  ), f, s;
  const _ = () => (
    /*button_binding*/
    t[40](e, r)
  ), u = () => (
    /*button_binding*/
    t[40](null, r)
  );
  function d() {
    return (
      /*click_handler_2*/
      t[41](
        /*i*/
        t[56]
      )
    );
  }
  return {
    c() {
      e = O("button"), l = O("img"), o = Ce(), vl(l.src, n = /*entry*/
      t[54].image.url) || F(l, "src", n), F(l, "title", i = /*entry*/
      t[54].caption || null), F(l, "data-testid", "thumbnail " + /*i*/
      (t[56] + 1)), F(l, "alt", ""), F(l, "loading", "lazy"), F(l, "class", "svelte-1p2as1x"), F(e, "class", "thumbnail-item thumbnail-small svelte-1p2as1x"), F(e, "aria-label", a = "Thumbnail " + /*i*/
      (t[56] + 1) + " of " + /*resolved_value*/
      t[16].length), Q(
        e,
        "selected",
        /*selected_index*/
        t[0] === /*i*/
        t[56]
      );
    },
    m(b, w) {
      re(b, e, w), P(e, l), P(e, o), _(), f || (s = kl(e, "click", d), f = !0);
    },
    p(b, w) {
      t = b, w[0] & /*resolved_value*/
      65536 && !vl(l.src, n = /*entry*/
      t[54].image.url) && F(l, "src", n), w[0] & /*resolved_value*/
      65536 && i !== (i = /*entry*/
      t[54].caption || null) && F(l, "title", i), w[0] & /*resolved_value*/
      65536 && a !== (a = "Thumbnail " + /*i*/
      (t[56] + 1) + " of " + /*resolved_value*/
      t[16].length) && F(e, "aria-label", a), r !== /*i*/
      t[56] && (u(), r = /*i*/
      t[56], _()), w[0] & /*selected_index*/
      1 && Q(
        e,
        "selected",
        /*selected_index*/
        t[0] === /*i*/
        t[56]
      );
    },
    d(b) {
      b && ae(e), u(), f = !1, s();
    }
  };
}
function Gt(t) {
  let e, l, n;
  return l = new So({
    props: {
      i18n: (
        /*i18n*/
        t[13]
      ),
      value: (
        /*resolved_value*/
        t[16]
      ),
      formatter: Ls
    }
  }), l.$on(
    "share",
    /*share_handler*/
    t[43]
  ), l.$on(
    "error",
    /*error_handler*/
    t[44]
  ), {
    c() {
      e = O("div"), Le(l.$$.fragment), F(e, "class", "icon-button svelte-1p2as1x");
    },
    m(i, o) {
      re(i, e, o), Me(l, e, null), n = !0;
    },
    p(i, o) {
      const a = {};
      o[0] & /*i18n*/
      8192 && (a.i18n = /*i18n*/
      i[13]), o[0] & /*resolved_value*/
      65536 && (a.value = /*resolved_value*/
      i[16]), l.$set(a);
    },
    i(i) {
      n || (A(l.$$.fragment, i), n = !0);
    },
    o(i) {
      V(l.$$.fragment, i), n = !1;
    },
    d(i) {
      i && ae(e), Fe(l);
    }
  };
}
function Xt(t) {
  let e, l, n, i, o;
  function a() {
    return (
      /*click_handler_3*/
      t[45](
        /*i*/
        t[56]
      )
    );
  }
  function r() {
    return (
      /*label_click_handler*/
      t[46](
        /*i*/
        t[56],
        /*entry*/
        t[54]
      )
    );
  }
  return l = new zs({
    props: {
      likeable: (
        /*likeable*/
        t[11]
      ),
      clickable: (
        /*clickable*/
        t[12]
      ),
      value: (
        /*entry*/
        t[54]
      ),
      action_label: (
        /*action_label*/
        t[6]
      )
    }
  }), l.$on("click", a), l.$on("label_click", r), {
    c() {
      e = O("div"), Le(l.$$.fragment), n = Ce(), F(e, "class", "thumbnail-item thumbnail-lg svelte-1p2as1x"), F(e, "aria-label", i = "Thumbnail " + /*i*/
      (t[56] + 1) + " of " + /*resolved_value*/
      t[16].length), Q(
        e,
        "selected",
        /*selected_index*/
        t[0] === /*i*/
        t[56]
      );
    },
    m(f, s) {
      re(f, e, s), Me(l, e, null), P(e, n), o = !0;
    },
    p(f, s) {
      t = f;
      const _ = {};
      s[0] & /*likeable*/
      2048 && (_.likeable = /*likeable*/
      t[11]), s[0] & /*clickable*/
      4096 && (_.clickable = /*clickable*/
      t[12]), s[0] & /*resolved_value*/
      65536 && (_.value = /*entry*/
      t[54]), s[0] & /*action_label*/
      64 && (_.action_label = /*action_label*/
      t[6]), l.$set(_), (!o || s[0] & /*resolved_value*/
      65536 && i !== (i = "Thumbnail " + /*i*/
      (t[56] + 1) + " of " + /*resolved_value*/
      t[16].length)) && F(e, "aria-label", i), (!o || s[0] & /*selected_index*/
      1) && Q(
        e,
        "selected",
        /*selected_index*/
        t[0] === /*i*/
        t[56]
      );
    },
    i(f) {
      o || (A(l.$$.fragment, f), o = !0);
    },
    o(f) {
      V(l.$$.fragment, f), o = !1;
    },
    d(f) {
      f && ae(e), Fe(l);
    }
  };
}
function Xs(t) {
  let e, l;
  const n = [
    /*load_more_button_props*/
    t[14]
  ];
  let i = {
    $$slots: { default: [Us] },
    $$scope: { ctx: t }
  };
  for (let o = 0; o < n.length; o += 1)
    i = As(i, n[o]);
  return e = new ks({ props: i }), e.$on(
    "click",
    /*click_handler_4*/
    t[47]
  ), {
    c() {
      Le(e.$$.fragment);
    },
    m(o, a) {
      Me(e, o, a), l = !0;
    },
    p(o, a) {
      const r = a[0] & /*load_more_button_props*/
      16384 ? Bs(n, [Vs(
        /*load_more_button_props*/
        o[14]
      )]) : {};
      a[0] & /*i18n, load_more_button_props*/
      24576 | a[1] & /*$$scope*/
      134217728 && (r.$$scope = { dirty: a, ctx: o }), e.$set(r);
    },
    i(o) {
      l || (A(e.$$.fragment, o), l = !0);
    },
    o(o) {
      V(e.$$.fragment, o), l = !1;
    },
    d(o) {
      Fe(e, o);
    }
  };
}
function Hs(t) {
  let e, l;
  return e = new en({ props: { margin: !1 } }), {
    c() {
      Le(e.$$.fragment);
    },
    m(n, i) {
      Me(e, n, i), l = !0;
    },
    p: Ns,
    i(n) {
      l || (A(e.$$.fragment, n), l = !0);
    },
    o(n) {
      V(e.$$.fragment, n), l = !1;
    },
    d(n) {
      Fe(e, n);
    }
  };
}
function Us(t) {
  let e = (
    /*i18n*/
    t[13](
      /*load_more_button_props*/
      t[14].value || /*load_more_button_props*/
      t[14].label || "Load More"
    ) + ""
  ), l;
  return {
    c() {
      l = yn(e);
    },
    m(n, i) {
      re(n, l, i);
    },
    p(n, i) {
      i[0] & /*i18n, load_more_button_props*/
      24576 && e !== (e = /*i18n*/
      n[13](
        /*load_more_button_props*/
        n[14].value || /*load_more_button_props*/
        n[14].label || "Load More"
      ) + "") && pn(l, e);
    },
    d(n) {
      n && ae(l);
    }
  };
}
function Ws(t) {
  let e, l;
  return e = new Kt({}), {
    c() {
      Le(e.$$.fragment);
    },
    m(n, i) {
      Me(e, n, i), l = !0;
    },
    i(n) {
      l || (A(e.$$.fragment, n), l = !0);
    },
    o(n) {
      V(e.$$.fragment, n), l = !1;
    },
    d(n) {
      Fe(e, n);
    }
  };
}
function Ys(t) {
  let e, l, n, i, o, a, r;
  kn(
    /*onwindowresize*/
    t[37]
  );
  let f = (
    /*show_label*/
    t[2] && Zt(t)
  );
  const s = [Gs, Os], _ = [];
  function u(d, b) {
    return !/*value*/
    d[7] || !/*resolved_value*/
    d[16] || /*resolved_value*/
    d[16].length === 0 ? 0 : 1;
  }
  return l = u(t), n = _[l] = s[l](t), {
    c() {
      f && f.c(), e = Ce(), n.c(), i = Is();
    },
    m(d, b) {
      f && f.m(d, b), re(d, e, b), _[l].m(d, b), re(d, i, b), o = !0, a || (r = kl(
        window,
        "resize",
        /*onwindowresize*/
        t[37]
      ), a = !0);
    },
    p(d, b) {
      /*show_label*/
      d[2] ? f ? (f.p(d, b), b[0] & /*show_label*/
      4 && A(f, 1)) : (f = Zt(d), f.c(), A(f, 1), f.m(e.parentNode, e)) : f && (Ne(), V(f, 1, 1, () => {
        f = null;
      }), De());
      let w = l;
      l = u(d), l === w ? _[l].p(d, b) : (Ne(), V(_[w], 1, 1, () => {
        _[w] = null;
      }), De(), n = _[l], n ? n.p(d, b) : (n = _[l] = s[l](d), n.c()), A(n, 1), n.m(i.parentNode, i));
    },
    i(d) {
      o || (A(f), A(n), o = !0);
    },
    o(d) {
      V(f), V(n), o = !1;
    },
    d(d) {
      d && (ae(e), ae(i)), f && f.d(d), _[l].d(d), a = !1, r();
    }
  };
}
function Js(t, e, l) {
  let n, i, o;
  var a = this && this.__awaiter || function(g, T, X, te) {
    function xe(Ie) {
      return Ie instanceof X ? Ie : new X(function($e) {
        $e(Ie);
      });
    }
    return new (X || (X = Promise))(function(Ie, $e) {
      function sl(Ve) {
        try {
          Sl(te.next(Ve));
        } catch (zl) {
          $e(zl);
        }
      }
      function zn(Ve) {
        try {
          Sl(te.throw(Ve));
        } catch (zl) {
          $e(zl);
        }
      }
      function Sl(Ve) {
        Ve.done ? Ie(Ve.value) : xe(Ve.value).then(sl, zn);
      }
      Sl((te = te.apply(g, T || [])).next());
    });
  }, r, f, s;
  let { object_fit: _ = "cover" } = e, { show_label: u = !0 } = e, { has_more: d = !1 } = e, { label: b } = e, { pending: w } = e, { action_label: y } = e, { value: C = null } = e, { columns: k = [2] } = e, { height: v = "auto" } = e, { preview: m } = e, { root: h } = e, { proxy_url: q } = e, { allow_preview: p = !0 } = e, { show_share_button: L = !1 } = e, { likeable: N } = e, { clickable: _e } = e, { show_download_button: W = !1 } = e, { i18n: J } = e, { selected_index: S = null } = e, { load_more_button_props: we = {} } = e, Z = [], ee = 0, G = 0, qe = 0;
  const le = Ps();
  let ue = !0, B = null, ce = C;
  S == null && m && (C != null && C.length) && (S = 0);
  let Ae = S;
  function Ze(g) {
    const T = g.target, X = g.clientX, xe = T.offsetWidth / 2;
    X < xe ? l(0, S = n) : l(0, S = i);
  }
  function Je(g) {
    switch (g.code) {
      case "Escape":
        g.preventDefault();
        break;
      case "ArrowLeft":
        g.preventDefault(), l(0, S = n);
        break;
      case "ArrowRight":
        g.preventDefault(), l(0, S = i);
        break;
    }
  }
  let c = [], de;
  function Te(g) {
    return a(this, void 0, void 0, function* () {
      var T;
      if (typeof g != "number" || (yield Rs(), c[g] === void 0))
        return;
      (T = c[g]) === null || T === void 0 || T.focus();
      const { left: X, width: te } = de.getBoundingClientRect(), { left: xe, width: Ie } = c[g].getBoundingClientRect(), sl = xe - X + Ie / 2 - te / 2 + de.scrollLeft;
      de && typeof de.scrollTo == "function" && de.scrollTo({
        left: sl < 0 ? 0 : sl,
        behavior: "smooth"
      });
    });
  }
  function Pe() {
    l(18, G = window.innerHeight), l(15, qe = window.innerWidth);
  }
  const yl = (g) => Ze(g), Ee = (g) => {
    if (g.stopPropagation(), o.liked) {
      l(21, o.liked = void 0, o), le("like", {
        index: S,
        value: o.image,
        liked: o.liked
      });
      return;
    }
    l(21, o.liked = !0, o), le("like", {
      index: S,
      value: o.image,
      liked: o.liked
    });
  };
  function Re(g, T) {
    Bt[g ? "unshift" : "push"](() => {
      c[T] = g, l(19, c);
    });
  }
  const Cl = (g) => l(0, S = g);
  function ql(g) {
    Bt[g ? "unshift" : "push"](() => {
      de = g, l(20, de);
    });
  }
  const Ke = (g) => {
    js(g.detail.description);
  };
  function ke(g) {
    Es.call(this, t, g);
  }
  const Qe = (g) => l(0, S = g), Cn = (g, T) => {
    le("click", { index: g, value: T });
  }, qn = () => {
    le("load_more");
  };
  function Sn() {
    ee = this.clientHeight, l(17, ee);
  }
  return t.$$set = (g) => {
    "object_fit" in g && l(1, _ = g.object_fit), "show_label" in g && l(2, u = g.show_label), "has_more" in g && l(3, d = g.has_more), "label" in g && l(4, b = g.label), "pending" in g && l(5, w = g.pending), "action_label" in g && l(6, y = g.action_label), "value" in g && l(7, C = g.value), "columns" in g && l(25, k = g.columns), "height" in g && l(8, v = g.height), "preview" in g && l(26, m = g.preview), "root" in g && l(27, h = g.root), "proxy_url" in g && l(28, q = g.proxy_url), "allow_preview" in g && l(9, p = g.allow_preview), "show_share_button" in g && l(10, L = g.show_share_button), "likeable" in g && l(11, N = g.likeable), "clickable" in g && l(12, _e = g.clickable), "show_download_button" in g && l(29, W = g.show_download_button), "i18n" in g && l(13, J = g.i18n), "selected_index" in g && l(0, S = g.selected_index), "load_more_button_props" in g && l(14, we = g.load_more_button_props);
  }, t.$$.update = () => {
    if (t.$$.dirty[0] & /*columns*/
    33554432)
      if (typeof k == "object" && k !== null)
        if (Array.isArray(k)) {
          const g = k.length;
          l(33, Z = Nl.map((T, X) => {
            var te;
            return [
              T.width,
              (te = k[X]) !== null && te !== void 0 ? te : k[g - 1]
            ];
          }));
        } else {
          let g = 0;
          l(33, Z = Nl.map((T) => {
            const X = k[T.key];
            return g = X ?? g, [T.width, g];
          }));
        }
      else
        l(33, Z = Nl.map((g) => [g.width, k]));
    if (t.$$.dirty[0] & /*window_width*/
    32768 | t.$$.dirty[1] & /*breakpointColumns*/
    4) {
      for (const [g, T] of [...Z].reverse())
        if (qe >= g)
          break;
    }
    t.$$.dirty[0] & /*value*/
    128 | t.$$.dirty[1] & /*was_reset*/
    8 && l(34, ue = C == null || C.length === 0 ? !0 : ue), t.$$.dirty[0] & /*value*/
    128 && l(16, B = C == null ? null : C.map((g) => g)), t.$$.dirty[0] & /*value, preview, selected_index*/
    67108993 | t.$$.dirty[1] & /*prev_value, was_reset*/
    24 && (ll(ce, C) || (ue ? (l(0, S = m && (C != null && C.length) ? S ?? 0 : null), l(34, ue = !1)) : l(0, S = S != null && C != null && S < C.length ? S : null), le("change"), l(35, ce = C))), t.$$.dirty[0] & /*selected_index, resolved_value, _a*/
    1073807361 | t.$$.dirty[1] & /*_b*/
    1 && (n = ((S ?? 0) + (l(30, r = B == null ? void 0 : B.length) !== null && r !== void 0 ? r : 0) - 1) % (l(31, f = B == null ? void 0 : B.length) !== null && f !== void 0 ? f : 0)), t.$$.dirty[0] & /*selected_index, resolved_value*/
    65537 | t.$$.dirty[1] & /*_c*/
    2 && (i = ((S ?? 0) + 1) % (l(32, s = B == null ? void 0 : B.length) !== null && s !== void 0 ? s : 0)), t.$$.dirty[0] & /*selected_index, resolved_value*/
    65537 | t.$$.dirty[1] & /*old_selected_index*/
    32 && S !== Ae && (l(36, Ae = S), S !== null && le("select", {
      index: S,
      value: B == null ? void 0 : B[S]
    })), t.$$.dirty[0] & /*allow_preview, selected_index*/
    513 && p && Te(S), t.$$.dirty[0] & /*selected_index, resolved_value*/
    65537 && l(21, o = S != null && B != null ? B[S] : null);
  }, [
    S,
    _,
    u,
    d,
    b,
    w,
    y,
    C,
    v,
    p,
    L,
    N,
    _e,
    J,
    we,
    qe,
    B,
    ee,
    G,
    c,
    de,
    o,
    le,
    Ze,
    Je,
    k,
    m,
    h,
    q,
    W,
    r,
    f,
    s,
    Z,
    ue,
    ce,
    Ae,
    Pe,
    yl,
    Ee,
    Re,
    Cl,
    ql,
    Ke,
    ke,
    Qe,
    Cn,
    qn,
    Sn
  ];
}
class Ks extends Fs {
  constructor(e) {
    super(), Ds(
      this,
      e,
      Js,
      Ys,
      Ts,
      {
        object_fit: 1,
        show_label: 2,
        has_more: 3,
        label: 4,
        pending: 5,
        action_label: 6,
        value: 7,
        columns: 25,
        height: 8,
        preview: 26,
        root: 27,
        proxy_url: 28,
        allow_preview: 9,
        show_share_button: 10,
        likeable: 11,
        clickable: 12,
        show_download_button: 29,
        i18n: 13,
        selected_index: 0,
        load_more_button_props: 14
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: Qs,
  add_flush_callback: xs,
  assign: $s,
  bind: ef,
  binding_callbacks: lf,
  check_outros: tf,
  create_component: Wl,
  destroy_component: Yl,
  detach: nf,
  get_spread_object: of,
  get_spread_update: sf,
  group_outros: ff,
  init: af,
  insert: rf,
  mount_component: Jl,
  safe_not_equal: _f,
  space: uf,
  transition_in: Ue,
  transition_out: nl
} = window.__gradio__svelte__internal, { createEventDispatcher: cf } = window.__gradio__svelte__internal;
function Ht(t) {
  let e, l;
  const n = [
    {
      autoscroll: (
        /*gradio*/
        t[25].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      t[25].i18n
    ) },
    /*loading_status*/
    t[1],
    {
      show_progress: (
        /*loading_status*/
        t[1].show_progress === "hidden" ? "hidden" : (
          /*has_more*/
          t[3] ? "minimal" : (
            /*loading_status*/
            t[1].show_progress
          )
        )
      )
    }
  ];
  let i = {};
  for (let o = 0; o < n.length; o += 1)
    i = $s(i, n[o]);
  return e = new ss({ props: i }), {
    c() {
      Wl(e.$$.fragment);
    },
    m(o, a) {
      Jl(e, o, a), l = !0;
    },
    p(o, a) {
      const r = a[0] & /*gradio, loading_status, has_more*/
      33554442 ? sf(n, [
        a[0] & /*gradio*/
        33554432 && {
          autoscroll: (
            /*gradio*/
            o[25].autoscroll
          )
        },
        a[0] & /*gradio*/
        33554432 && { i18n: (
          /*gradio*/
          o[25].i18n
        ) },
        a[0] & /*loading_status*/
        2 && of(
          /*loading_status*/
          o[1]
        ),
        a[0] & /*loading_status, has_more*/
        10 && {
          show_progress: (
            /*loading_status*/
            o[1].show_progress === "hidden" ? "hidden" : (
              /*has_more*/
              o[3] ? "minimal" : (
                /*loading_status*/
                o[1].show_progress
              )
            )
          )
        }
      ]) : {};
      e.$set(r);
    },
    i(o) {
      l || (Ue(e.$$.fragment, o), l = !0);
    },
    o(o) {
      nl(e.$$.fragment, o), l = !1;
    },
    d(o) {
      Yl(e, o);
    }
  };
}
function df(t) {
  var f;
  let e, l, n, i, o = (
    /*loading_status*/
    t[1] && Ht(t)
  );
  function a(s) {
    t[29](s);
  }
  let r = {
    pending: (
      /*loading_status*/
      ((f = t[1]) == null ? void 0 : f.status) === "pending"
    ),
    likeable: (
      /*likeable*/
      t[10]
    ),
    clickable: (
      /*clickable*/
      t[11]
    ),
    label: (
      /*label*/
      t[4]
    ),
    action_label: (
      /*action_label*/
      t[5]
    ),
    value: (
      /*value*/
      t[9]
    ),
    root: (
      /*root*/
      t[23]
    ),
    proxy_url: (
      /*proxy_url*/
      t[24]
    ),
    show_label: (
      /*show_label*/
      t[2]
    ),
    object_fit: (
      /*object_fit*/
      t[21]
    ),
    load_more_button_props: (
      /*_load_more_button_props*/
      t[26]
    ),
    has_more: (
      /*has_more*/
      t[3]
    ),
    columns: (
      /*columns*/
      t[15]
    ),
    height: (
      /*height*/
      t[17]
    ),
    preview: (
      /*preview*/
      t[18]
    ),
    gap: (
      /*gap*/
      t[16]
    ),
    allow_preview: (
      /*allow_preview*/
      t[19]
    ),
    show_share_button: (
      /*show_share_button*/
      t[20]
    ),
    show_download_button: (
      /*show_download_button*/
      t[22]
    ),
    i18n: (
      /*gradio*/
      t[25].i18n
    )
  };
  return (
    /*selected_index*/
    t[0] !== void 0 && (r.selected_index = /*selected_index*/
    t[0]), l = new Ks({ props: r }), lf.push(() => ef(l, "selected_index", a)), l.$on(
      "click",
      /*click_handler*/
      t[30]
    ), l.$on(
      "change",
      /*change_handler*/
      t[31]
    ), l.$on(
      "like",
      /*like_handler*/
      t[32]
    ), l.$on(
      "select",
      /*select_handler*/
      t[33]
    ), l.$on(
      "share",
      /*share_handler*/
      t[34]
    ), l.$on(
      "error",
      /*error_handler*/
      t[35]
    ), l.$on(
      "load_more",
      /*load_more_handler*/
      t[36]
    ), {
      c() {
        o && o.c(), e = uf(), Wl(l.$$.fragment);
      },
      m(s, _) {
        o && o.m(s, _), rf(s, e, _), Jl(l, s, _), i = !0;
      },
      p(s, _) {
        var d;
        /*loading_status*/
        s[1] ? o ? (o.p(s, _), _[0] & /*loading_status*/
        2 && Ue(o, 1)) : (o = Ht(s), o.c(), Ue(o, 1), o.m(e.parentNode, e)) : o && (ff(), nl(o, 1, 1, () => {
          o = null;
        }), tf());
        const u = {};
        _[0] & /*loading_status*/
        2 && (u.pending = /*loading_status*/
        ((d = s[1]) == null ? void 0 : d.status) === "pending"), _[0] & /*likeable*/
        1024 && (u.likeable = /*likeable*/
        s[10]), _[0] & /*clickable*/
        2048 && (u.clickable = /*clickable*/
        s[11]), _[0] & /*label*/
        16 && (u.label = /*label*/
        s[4]), _[0] & /*action_label*/
        32 && (u.action_label = /*action_label*/
        s[5]), _[0] & /*value*/
        512 && (u.value = /*value*/
        s[9]), _[0] & /*root*/
        8388608 && (u.root = /*root*/
        s[23]), _[0] & /*proxy_url*/
        16777216 && (u.proxy_url = /*proxy_url*/
        s[24]), _[0] & /*show_label*/
        4 && (u.show_label = /*show_label*/
        s[2]), _[0] & /*object_fit*/
        2097152 && (u.object_fit = /*object_fit*/
        s[21]), _[0] & /*_load_more_button_props*/
        67108864 && (u.load_more_button_props = /*_load_more_button_props*/
        s[26]), _[0] & /*has_more*/
        8 && (u.has_more = /*has_more*/
        s[3]), _[0] & /*columns*/
        32768 && (u.columns = /*columns*/
        s[15]), _[0] & /*height*/
        131072 && (u.height = /*height*/
        s[17]), _[0] & /*preview*/
        262144 && (u.preview = /*preview*/
        s[18]), _[0] & /*gap*/
        65536 && (u.gap = /*gap*/
        s[16]), _[0] & /*allow_preview*/
        524288 && (u.allow_preview = /*allow_preview*/
        s[19]), _[0] & /*show_share_button*/
        1048576 && (u.show_share_button = /*show_share_button*/
        s[20]), _[0] & /*show_download_button*/
        4194304 && (u.show_download_button = /*show_download_button*/
        s[22]), _[0] & /*gradio*/
        33554432 && (u.i18n = /*gradio*/
        s[25].i18n), !n && _[0] & /*selected_index*/
        1 && (n = !0, u.selected_index = /*selected_index*/
        s[0], xs(() => n = !1)), l.$set(u);
      },
      i(s) {
        i || (Ue(o), Ue(l.$$.fragment, s), i = !0);
      },
      o(s) {
        nl(o), nl(l.$$.fragment, s), i = !1;
      },
      d(s) {
        s && nf(e), o && o.d(s), Yl(l, s);
      }
    }
  );
}
function mf(t) {
  let e, l;
  return e = new On({
    props: {
      visible: (
        /*visible*/
        t[8]
      ),
      variant: "solid",
      padding: !1,
      elem_id: (
        /*elem_id*/
        t[6]
      ),
      elem_classes: (
        /*elem_classes*/
        t[7]
      ),
      container: (
        /*container*/
        t[12]
      ),
      scale: (
        /*scale*/
        t[13]
      ),
      min_width: (
        /*min_width*/
        t[14]
      ),
      allow_overflow: !1,
      $$slots: { default: [df] },
      $$scope: { ctx: t }
    }
  }), {
    c() {
      Wl(e.$$.fragment);
    },
    m(n, i) {
      Jl(e, n, i), l = !0;
    },
    p(n, i) {
      const o = {};
      i[0] & /*visible*/
      256 && (o.visible = /*visible*/
      n[8]), i[0] & /*elem_id*/
      64 && (o.elem_id = /*elem_id*/
      n[6]), i[0] & /*elem_classes*/
      128 && (o.elem_classes = /*elem_classes*/
      n[7]), i[0] & /*container*/
      4096 && (o.container = /*container*/
      n[12]), i[0] & /*scale*/
      8192 && (o.scale = /*scale*/
      n[13]), i[0] & /*min_width*/
      16384 && (o.min_width = /*min_width*/
      n[14]), i[0] & /*loading_status, likeable, clickable, label, action_label, value, root, proxy_url, show_label, object_fit, _load_more_button_props, has_more, columns, height, preview, gap, allow_preview, show_share_button, show_download_button, gradio, selected_index*/
      134188607 | i[1] & /*$$scope*/
      128 && (o.$$scope = { dirty: i, ctx: n }), e.$set(o);
    },
    i(n) {
      l || (Ue(e.$$.fragment, n), l = !0);
    },
    o(n) {
      nl(e.$$.fragment, n), l = !1;
    },
    d(n) {
      Yl(e, n);
    }
  };
}
function bf(t, e, l) {
  let { loading_status: n } = e, { show_label: i } = e, { has_more: o } = e, { label: a } = e, { action_label: r } = e, { elem_id: f = "" } = e, { elem_classes: s = [] } = e, { visible: _ = !0 } = e, { value: u = null } = e, { likeable: d } = e, { clickable: b } = e, { container: w = !0 } = e, { scale: y = null } = e, { min_width: C = void 0 } = e, { columns: k = [2] } = e, { gap: v = 8 } = e, { height: m = "auto" } = e, { preview: h } = e, { allow_preview: q = !0 } = e, { selected_index: p = null } = e, { show_share_button: L = !1 } = e, { object_fit: N = "cover" } = e, { show_download_button: _e = !1 } = e, { root: W } = e, { proxy_url: J } = e, { gradio: S } = e, { load_more_button_props: we = {} } = e, Z = {};
  const ee = cf(), G = (c) => {
    S.dispatch("like", c);
  };
  function qe(c) {
    p = c, l(0, p);
  }
  const le = (c) => S.dispatch("click", c.detail), ue = () => S.dispatch("change", u), B = (c) => G(c.detail), ce = (c) => S.dispatch("select", c.detail), Ae = (c) => S.dispatch("share", c.detail), Ze = (c) => S.dispatch("error", c.detail), Je = () => {
    S.dispatch("load_more", u);
  };
  return t.$$set = (c) => {
    "loading_status" in c && l(1, n = c.loading_status), "show_label" in c && l(2, i = c.show_label), "has_more" in c && l(3, o = c.has_more), "label" in c && l(4, a = c.label), "action_label" in c && l(5, r = c.action_label), "elem_id" in c && l(6, f = c.elem_id), "elem_classes" in c && l(7, s = c.elem_classes), "visible" in c && l(8, _ = c.visible), "value" in c && l(9, u = c.value), "likeable" in c && l(10, d = c.likeable), "clickable" in c && l(11, b = c.clickable), "container" in c && l(12, w = c.container), "scale" in c && l(13, y = c.scale), "min_width" in c && l(14, C = c.min_width), "columns" in c && l(15, k = c.columns), "gap" in c && l(16, v = c.gap), "height" in c && l(17, m = c.height), "preview" in c && l(18, h = c.preview), "allow_preview" in c && l(19, q = c.allow_preview), "selected_index" in c && l(0, p = c.selected_index), "show_share_button" in c && l(20, L = c.show_share_button), "object_fit" in c && l(21, N = c.object_fit), "show_download_button" in c && l(22, _e = c.show_download_button), "root" in c && l(23, W = c.root), "proxy_url" in c && l(24, J = c.proxy_url), "gradio" in c && l(25, S = c.gradio), "load_more_button_props" in c && l(28, we = c.load_more_button_props);
  }, t.$$.update = () => {
    t.$$.dirty[0] & /*_load_more_button_props, load_more_button_props*/
    335544320 && l(26, Z = Object.assign(Object.assign({}, Z), we)), t.$$.dirty[0] & /*selected_index*/
    1 && ee("prop_change", { selected_index: p });
  }, [
    p,
    n,
    i,
    o,
    a,
    r,
    f,
    s,
    _,
    u,
    d,
    b,
    w,
    y,
    C,
    k,
    v,
    m,
    h,
    q,
    L,
    N,
    _e,
    W,
    J,
    S,
    Z,
    G,
    we,
    qe,
    le,
    ue,
    B,
    ce,
    Ae,
    Ze,
    Je
  ];
}
class gf extends Qs {
  constructor(e) {
    super(), af(
      this,
      e,
      bf,
      mf,
      _f,
      {
        loading_status: 1,
        show_label: 2,
        has_more: 3,
        label: 4,
        action_label: 5,
        elem_id: 6,
        elem_classes: 7,
        visible: 8,
        value: 9,
        likeable: 10,
        clickable: 11,
        container: 12,
        scale: 13,
        min_width: 14,
        columns: 15,
        gap: 16,
        height: 17,
        preview: 18,
        allow_preview: 19,
        selected_index: 0,
        show_share_button: 20,
        object_fit: 21,
        show_download_button: 22,
        root: 23,
        proxy_url: 24,
        gradio: 25,
        load_more_button_props: 28
      },
      null,
      [-1, -1]
    );
  }
}
export {
  Ks as BaseGallery,
  gf as default
};
