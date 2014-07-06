(import [django.shortcuts [render-to-response render]])
(import [django.http [HttpResponse]])


(defn main [request]
  (render-to-response "forum/home.html" {}))

