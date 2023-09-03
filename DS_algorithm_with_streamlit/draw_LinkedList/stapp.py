import streamlit as st
import networkx as nx
import plotly.graph_objects as go
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def draw_linked_list(head):
    G = nx.DiGraph()
    pos = {}
    x = 0
    current = head
    while current:
        G.add_node(current.value)
        pos[current.value] = (x, 0)
        if current.next:
            G.add_edge(current.value, current.next.value)
        current = current.next
        x += 1

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=2, color='black'),
        hoverinfo='none',
        mode='lines')

    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=0),
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False))
    )
    return fig


def app():
    st.title('Linked List Visualization')

    # Input for linked list values
    user_input = st.text_input(
        'Enter linked list values separated by commas:', '1,2,3')

    # Parse input and create linked list
    values = [int(x.strip()) for x in user_input.split(',')]
    head = None
    current = None
    for value in reversed(values):
        head = ListNode(value, current)
        current = head

    # Draw linked list
    fig = draw_linked_list(head)
    st.plotly_chart(fig)


if __name__ == "__main__":
    app()
