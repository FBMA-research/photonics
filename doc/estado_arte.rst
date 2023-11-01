Estado del arte.
----------------

Cristales fotónicos
~~~~~~~~~~~~~~~~~~

Los cristales fotónicos (CF) son materiales ópticos con una microestrucutra periódica a escala de la longitud de la luz. Los
cristales fotónicos ofrecen un novedosa manera de manipular las ondas electromagnéticas, ellos operan bajo el principio de
los gaps fotónicos, regiones donde los fotones no pueden propagarse [1]. Los CF se clasifican en 1D, 2D y 3D basados en la
periodicidad de la estructura [2]. Estos materiales tienen aplicaciones in guías de onda filtros ópticos y circuitos fotónicos
integrados [3].

Ecuaciones de Maxwell en la simulación de cristales fotónicos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Las ecuaciones de Maxwell son el fundamento para comprender el comportamiento electromagnético de los CF [4]. La aplicación de
condiciones periódicas adecuadas es crucial para la simulación y resultados consistentes [5]. Métodos como elementos finitos
(FDTD) y plano de expansión de onda (PWE) son usados para resolver las ecuaciones de Maxwell en este contexto [6].

El punto de partida para cualquier solucionador FDTD son las partes derivadas del tiempo de las ecuaciones de Maxwell, que en
su forma más simple se pueden escribir.

.. math::
    \begin{aligned}
    \frac{\partial \textbf{B}}{\partial t} &= -\nabla \times \textbf{E} - \textbf{J}_{\textbf{B}} \\
    \frac{\partial \textbf{D}}{\partial t} &= +\nabla \times \textbf{H} - \textbf{J}
    \end{aligned}

Donde :math:`\textbf{E}` y :math:`\textbf{H}` son el campo eléctrico macroscópico y el campo magnético respectivos, :math:`\textbf{E}`
y :math:`\textbf{B}` es el desplazamiento eléctrico y el campo magnético inducido respectivamente, :math:`\textbf{J}` es la
densidad de corriente de carga eléctrica y :math:`\textbf{J}_{\textbf{B}}` es una densidad de carga magnética.

.. admonition:: Problema de valor inicial
    :class: note

    En los cálculos del dominio del tiempo normalmente se resuelve el problema inicial como un problema de valor inicial
    donde los campos y las corrientes son 0 para un tiempo :math:`t < 0`. Luego, los valores distintos de 0 evolucionan en
    respuesta a algunas corrientes :math:`\text{J}(x, t)` y/o :math:`\text{J}_{\text{B}}(x, t)`.


Desarrollo histórico.
~~~~~~~~~~~~~~~~~~~~

El concepto de CF fue introducido en los años 80 y esto represento contribuciones tanto teóricas como experimentales [7].
Investigadores como Eli Yablonovitch and Sajeev John han hecho desarrollos pioneros en este campo [8].

El software MEEP
~~~~~~~~~~~~~~~~

.. admonition:: ¿Qué significa ``MEEP``?
    :class: hint

    ``MEEP`` son las siglas para "MIT Electromagnetic Equation Propagation"

Meep ofrece una plataforma para la simulación de una amplia matriz de arreglos fotónicos [9]. Algunas de sus ventajas es que es
de  uso libre y es flexible para ser modificado por el usuario [10]. Algunas de sus limitaciones es el largo tiempo de computo
para simulaciones 3D [11].

Una filosofía del diseño central del MEEP es proporcionar la ilusión de espacio y tiempos contínuos, enmascarar la discretización
subyascente del usuario tanto como sea posible.

Aplicaciones tecnológicas recientes de los CF.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- En comunicaciones ópticas: Usado en la creación switches ultra rápidos [12].
- Sensado: Potencial para biosensores altamente sensibles [13].
- Recolección de energía: Los CF pueden mejorar la eficiencia de las celdas solares [14].

Enfoques y limitaciones existentes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Además de Meep también existen otras herramientas como COMSOL y Lumerical, pero tienen sus limitaciones [15].  La teoría del medio
eficaz y la teoría del modo acoplado son algunos de los enfoques analíticos [16]. Los métodos actuales suelen pasar por alto los
efectos no lineales y los fenómenos cuánticos [17].

Perspectiva del futuro
~~~~~~~~~~~~~~~~~~~~~

El aprendizaje automático y la computación cuántica son vías potenciales para mejorar las simulaciones [18]. La investigación sobre
fotónica topológica y efectos cuánticos podría revolucionar este campo [19].