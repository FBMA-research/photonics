This is a little notebook test
==============================

This little test is to try and run markdown and code cells and see if
sphinx can renderize them via the extensions installed in the
``documentation.yaml`` workflow. Let’s see a little latex here:

.. math::  \frac{d}{dx} \int_a^b f(x) \; dx = f(b)\frac{db}{dx} - f(a)\frac{da}{dx} 

Now, let’s see a little code:

.. code:: ipython3

    def say_hi(name):
        return f"hi {name}, cool name!"
    
    print(say_hi("Juan"))


.. parsed-literal::

    hi Juan, cool name!
    

Let’s see notes and warnings in jupyter notebook!:

\```{note} ¡Aquí hay una nota!

.. container:: alert alert-block alert-info

   Tip: Usa cajas azules (alert-info) para consejos y notas. Si es una
   nota, no tienes que incluir la palabra “Nota”.

.. container:: alert alert-block alert-warning

   Advertencia: Usa cajas amarillas (alert-warning) para advertencias.

Now, let’s see tabulations, bullets and tables!

   this is a tabulation

   This is very helpful to denote delimited text

-  This is a bullet 1

   -  this is a bullet 2
   -  this is another bullet 2

Let’s see a table:

===== ========= =========
index feature 1 feature 2
===== ========= =========
0     3.5       4.1
1     6.7       8.9
===== ========= =========


