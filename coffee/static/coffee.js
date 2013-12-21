moment.lang('nb');
var updating = {'status': false, 'stats': false};
function updateStatusText(data){
  $('#status').html(
    'Kaffetrakteren er ' +
    ( data.status ? 'på' : 'av' ) +
    '. Den ble sist skrudd på ' +
    moment(data.last_start, 'YYYY-MM-DD HH:mm').fromNow() + '.'
  );
}
function updateStatus(){
  if (!updating.status) {
    updating.status = true;
    $.getJSON('/api/status', function(data){
      updateStatusText(data.coffee);
      updating.status = false;
    });
  }
  if (!updating.stats) {
    updating.stats = true;
    $.getJSON('http://kaffe.abakus.no/api/stats', function(data){
      var c = $('#chart'),
        ctx = c.get(0).getContext('2d'),
        chart = new Chart(ctx),
        transform = function(d) {
          var out = {
              labels: [],
              datasets: []
            },
            dataset = {
              fillColor : 'rgba(220,220,220,0.5)',
              strokeColor : '#ec483c',
              pointColor : '#ec483c',
              pointStrokeColor : '#e23e32',
              data : []
            };
          for(var k in d){
            out.labels.push(k);
          }
          out.labels.sort();
          for(var i = 0; i < out.labels.length; i++){
            dataset.data.push(parseInt(d[out.labels[i]], 10));
          }
          out.datasets.push(dataset);
          console.log(out);
          return out;
        };
      chart.Line(transform(data.stats), {
        animation: false
      });
      c.css('width', '');
      updating.stats = false;
    });
  }

}
$('.btn-update').on('click', function(e){
  e.preventDefault();
  updateStatus(); 
});
