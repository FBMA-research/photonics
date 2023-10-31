Resultados preliminares
-----------------------

.. _github: https://github.com/FBMA-research/photonics

Se logró replicar los resultados de las dispersiones del cristal a partir de simulaciones iniciales con el uso del software COMSOL
comparando el modo TM y añadiendo los modos TE y TM calculados en el software libre MEEP.

Se anexó un diseño personalizado en MEEP para la incorporación de las geometrías específicas del cristal fotónico.

Se está implementando la documentación del desarrollo `github`_.

Conclusiones
------------

Las implementaciones de software libre como el Meep permiten un ajuste personalizado del software a las necesidades de simulación.
Con esta plataforma tecnológica se agregaron nuevas implementaciones para la captura de las geometrías y el ajuste de la zona de
Brillouin.

Se está adaptando el software para el cómputo en un cluster que nos permita hacer simulaciones más robustas con un amplio número de
variables a estudiar.