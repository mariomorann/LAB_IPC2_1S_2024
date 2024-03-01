# https://graphviz.readthedocs.io/en/stable/manual.html
# pip install graphviz

import graphviz


def main():
    dot = graphviz.Graph(filename='archivo')
    dot.node('tab',
    """<<table>
        <tr>
            <td> A </td>
            <td> B </td>
            <td> C </td>
        </tr>
        <tr>
            <td> A </td>
            <td> B </td>
            <td> C </td>
        </tr>
        <tr>
            <td> A </td>
            <td> B </td>
            <td> C </td>
        </tr>
    </table>>"""
    )

    dot.render(directory='', view=True)  


if __name__ == "__main__":
    main()