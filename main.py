{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rQBrcCM2qn2n"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "from matplotlib.animation import FuncAnimation\n",
        "from IPython.display import HTML"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qxO0Wb7rq8Ce"
      },
      "outputs": [],
      "source": [
        "earth_x = 0\n",
        "earth_y = 0\n",
        "\n",
        "sat_x = 10\n",
        "sat_y = 0\n",
        "\n",
        "vx= 0\n",
        "vy = 0.4\n",
        "\n",
        "orbit_x = []\n",
        "orbit_y = []\n",
        "\n",
        "gravity = 0.01"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2HqaA0Tst9Dm"
      },
      "outputs": [],
      "source": [
        "for i in range(1000):\n",
        "\n",
        "  dx = earth_x - sat_x\n",
        "  dy = earth_y - sat_y\n",
        "\n",
        "  dist = np.sqrt(dx**2 + dy**2)\n",
        "\n",
        "  ax_force = gravity * dx / dist\n",
        "  ay_force = gravity * dy / dist\n",
        "\n",
        "  vx += ax_force\n",
        "  vy += ay_force\n",
        "\n",
        "  sat_x += vx\n",
        "  sat_y += vy\n",
        "\n",
        "  orbit_x.append(sat_x)\n",
        "  orbit_y.append(sat_y)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qRXBwjrQwgbf"
      },
      "outputs": [],
      "source": [
        "fig, ax = plt.subplots(figsize=(10,10))\n",
        "\n",
        "ax.set_xlim(-15,15)\n",
        "ax.set_ylim(-15,15)\n",
        "\n",
        "ax.scatter(0,0,s=200,label=\"Earth\")\n",
        "\n",
        "satellite, = ax.plot([], [], \"o\", label=\"Satellite\")\n",
        "trail, = ax.plot([], [], label=\"Orbit Path\")\n",
        "\n",
        "ax.legend()\n",
        "\n",
        "def update(frame):\n",
        "\n",
        "    satellite.set_data(\n",
        "       [orbit_x[frame]],\n",
        "                 [orbit_y[frame]]\n",
        "                        )\n",
        "    trail.set_data(orbit_x[:frame], orbit_y[:frame])\n",
        "\n",
        "    return satellite, trail\n",
        "\n",
        "ani = FuncAnimation(fig, update, frames=len(orbit_x),interval=20,blit=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "akJk6wde8tWb"
      },
      "outputs": [],
      "source": [
        "HTML(ani.to_jshtml())"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ani.save(\"orbit.gif\")"
      ],
      "metadata": {
        "id": "a92dl00UImM7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "files.download(\"orbit.gif\")"
      ],
      "metadata": {
        "id": "NNcNxIcrIqSg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "872025a7"
      },
      "outputs": [],
      "source": [
        "plt.rcParams['animation.embed_limit'] = 1000.0 # Set the limit to 1000 MB, adjust as needed"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
