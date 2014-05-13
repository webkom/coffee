moment.lang('nb');
var updating = {'status': false, 'stats': false},
  jsChart,
  transform = function(d) {
    var out = {
        labels: [],
        datasets: [],
        maxValue: function () {
          return Math.max.apply(Math, this.datasets[0].data);
        }
      },
      dataset = {
        fillColor : 'rgba(220,220,220,0.5)',
        strokeColor : '#ec483c',
        pointColor : '#ec483c',
        pointStrokeColor : '#e23e32',
        data : []
      };
    for (var k in d) {
      out.labels.push(k);
    }
    out.labels.sort();
    if (out.labels.length > 10) {
      out.labels = out.labels.slice(-10);
    }
    for (var i = 0; i < out.labels.length; i++) {
      dataset.data.push(parseInt(d[out.labels[i]], 10));
      out.labels[i] = moment(out.labels[i], 'YYYY-MM-DD').format('DD-MM');
    }
    out.datasets.push(dataset);
    return out;
  },
  updateStatusText = function (data) {
    $('#status').html(
      'Kaffetrakteren er ' +
      ( data.status === true ? 'på' : 'av' ) +
      '. Den ble sist skrudd på ' +
      moment(data.last_start, 'YYYY-MM-DD HH:mm').fromNow() + '.'
    );
  },
  updateStatus = function () {
    if (!updating.status) {
      updating.status = true;
      $.getJSON('/api/status', function(data){
        updateStatusText(data.coffee);
        updating.status = false;
      });
    }

    if (!updating.stats) {
      updating.stats = true;
      $.getJSON('/api/stats', function(data){
        var c = $('#chart'),
          ctx = c.get(0).getContext('2d'),
          model = transform(data.stats),
          stepWidth = 2,
          steps = model.maxValue() / stepWidth,
          options = {
            scaleOverride: true,
            scaleSteps: steps,
            scaleStepWidth: stepWidth,
            scaleStartValue: 0,
            animation: false
          };
        if (!jsChart) {
          jsChart = new Chart(ctx);
          jsChart.Line(model, options);
        }
        else {
          jsChart.Line(model, options);
        }
        updating.stats = false;
      });
    }

  };
$('.btn-update').on('click', function(e){
  e.preventDefault();
  updateStatus(); 
});
