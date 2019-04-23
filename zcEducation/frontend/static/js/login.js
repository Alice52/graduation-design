$(function () {
  $('.imgslide').unslider({
    speed: 500,
    delay: 3000,
    complete: function () {},
    keys: true,
    dots: true,
    fluid: false
  })
  var unslider = $('.imgslide').unslider()
  $('.unslider-arrow').click(function () {
    var fn = this.className.split(' ')[1]
    unslider.data('unslider')[fn]()
  })

  $('.tab > h2').click(function () {
    var _self = $(this),
      index = _self.index()
    _self
      .addClass('active')
      .siblings()
      .removeClass('active')
    $('.tab-form')
      .eq(index)
      .removeClass('hide')
      .siblings('.tab-form')
      .addClass('hide')
  })

  // input的focus和blur效果
  $('input[type=text]').focus(function () {
    $(this)
      .parent()
      .removeClass('blur')
      .addClass('focus')
  })
  $('input[type=text]').blur(function () {
    $(this)
      .parent()
      .removeClass('focus')
      .addClass('blur')
  })
  // input的focus和blur效果
  $('input[type=password]').focus(function () {
    $(this)
      .parent()
      .removeClass('blur')
      .addClass('focus')
  })
  $('input[type=password]').blur(function () {
    $(this)
      .parent()
      .removeClass('focus')
      .addClass('blur')
  })

  // 弹出框关闭按钮
  $('.jsCloseDialog').on('click', function () {
    $(this)
      .parents('.dialogbox')
      .hide()
    $('#dialogBg').hide()
    if ($(this).siblings('form')[0]) {
      $(this)
        .siblings('form')[0]
        .reset()
    }
  })
})
