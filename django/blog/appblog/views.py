from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
    autore1 = request.GET.get("autore1") or "autore 1"
    autore2 = request.GET.get("autore2") or "autore 2"
    return render(request,'index.html', { 'autore1' : autore1, 'autore2' : autore2 })

def contatti(request):
    autore1 = request.GET.get("autore1") or "autore 1"
    autore2 = request.GET.get("autore2") or "autore 2"
    return render(request,'contatti.html', { 'autore1' : autore1, 'autore2' : autore2 })

def autore1(request):
    autore1 = request.GET.get("autore1") or "autore 1"
    autore2 = request.GET.get("autore2") or "autore 2"
    msg = "Articoli di "
    dati = [{
        'titolo':"La casa sulla collina",
        'data': "12/10/2011",
        'corpo': "Voluptatibus blanditiis harum rem. Explicabo ab quibusdam vel nesciunt reiciendis corrupti aliquam deserunt delectus mollitia aliquid? Nemo velit repudiandae quis itaque quae doloremque perferendis, debitis distinctio expedita nihil ratione vero, possimus assumenda numquam facere expedita fuga deserunt iure architecto. Sequi deleniti cum provident vero vel."
    },
    {
        'titolo':"Il testimone di nozze",
        'data': "27/10/2012",
        'corpo': "Asperiores ullam doloremque rerum magnam ad explicabo in labore, quis sunt eligendi rem praesentium, eum tenetur illum quo laborum sint ut vitae aspernatur eligendi totam maiores, dolorum eos itaque tempore, sunt provident ratione eligendi maiores non consequatur maxime sit temporibus? Neque consectetur error aperiam ipsam corporis odit deleniti, ullam possimus laboriosam dolores ducimus commodi magni libero consequatur. Nobis sequi alias velit delectus ipsum incidunt. Laboriosam necessitatibus impedit doloribus id eos recusandae, excepturi molestiae fuga cumque quibusdam maiores tempore voluptates quidem saepe, reprehenderit perferendis possimus natus voluptate laboriosam culpa officia labore in id, adipisci facilis laborum voluptatum obcaecati accusantium, vero consequatur cupiditate asperiores numquam ipsa? Reprehenderit quis provident possimus placeat recusandae dignissimos. Porro perspiciatis ab, sit consectetur culpa possimus veniam?"
    }]
    return render(request,'autore1.html', { 'autore1' : autore1, 'autore2' : autore2, 'articoli':dati, 'intestazione':msg })

def autore2(request):
    autore1 = request.GET.get("autore1") or "autore 1"
    autore2 = request.GET.get("autore2") or "autore 2"
    msg = "Articoli di "
    dati = [{
        'titolo':"La battaglia di Zama",
        'data': "30/02/2003",
        'corpo': "Excepturi reiciendis perferendis odio nostrum illo. Perferendis iste unde, mollitia facere accusamus corporis sunt itaque? Sed rem natus ad ducimus autem voluptas nesciunt laboriosam, mollitia sint aut quidem minus et consequatur quia repudiandae, a officia praesentium nihil recusandae natus blanditiis asperiores voluptatem quam possimus debitis, obcaecati dignissimos laudantium aliquam dicta voluptatem, delectus ut accusantium obcaecati. Similique quia esse accusamus iusto nihil perferendis quos laborum excepturi odio quibusdam, consequatur repellendus neque voluptate vel, ad reprehenderit harum illo iusto ullam? Pariatur dolorum reprehenderit in, voluptas recusandae natus ipsum quam vero doloremque minima, neque incidunt vero quasi, tenetur enim facilis voluptate nemo ad error. Commodi porro quod tenetur consequuntur voluptatibus quo nulla, quos magnam hic?"
    },
    {
        'titolo':"Il processo di Norimberga",
        'data': "03/07/2005",
        'corpo': "Beatae consequatur necessitatibus optio dignissimos nobis enim quidem aspernatur a sit, voluptatum reprehenderit tenetur nisi placeat vel deleniti voluptatem fugit aliquam maxime, reprehenderit ipsa esse voluptatibus. Quidem fugiat ex neque adipisci doloribus pariatur officiis."
    },
    {
        'titolo':"L'età dell'oro",
        'data': "07/11/2009",
        'corpo': "Reiciendis deleniti esse optio magni molestiae vel, tempore officiis quidem, architecto harum nobis minus magni vel rerum. Voluptatum aliquid sint sed impedit voluptate maiores hic dolor ullam esse, sequi similique aperiam facilis culpa quia vero exercitationem ipsam delectus hic, iure sunt rem odio accusantium magni facilis quas officia amet, minima repellat praesentium itaque voluptatum ad natus? Voluptas repudiandae qui, odit recusandae quas voluptatum rerum voluptas, esse id cum commodi sit, accusamus id eveniet repellat delectus a temporibus expedita."
    },
    {
        'titolo':"L'attesa dell'evento",
        'data': "08/09/2015",
        'corpo': "Similique sequi recusandae quaerat, voluptates fugit suscipit, tempore modi quasi eveniet provident quis a soluta officia, sequi veritatis officiis molestiae ut dolorum ex molestias, quod iure dolores ratione quas consectetur vel placeat quis numquam nihil. Dignissimos similique aliquid corrupti cum debitis ab provident sit, porro quo eaque officia. Numquam saepe error ipsam et aperiam fuga ad commodi temporibus recusandae, consequuntur asperiores doloremque similique magni placeat eum incidunt fugit porro rerum, iure magni commodi ea illo sit saepe eveniet expedita molestias. Nobis maiores et, tenetur quibusdam incidunt beatae repellat minus explicabo vero consectetur quas earum autem? Sapiente totam adipisci dolore provident esse at? Facere eos corporis dolore cum dolorum possimus eum, dolores ipsa cumque dolore dolorem magnam libero est facere, earum impedit deserunt at recusandae similique quas nihil aut ipsam. Minima dolor amet at, nisi deleniti ex odit?"
    }]
    return render(request,'autore2.html', { 'autore1' : autore1, 'autore2' : autore2, 'articoli':dati, 'intestazione':msg })