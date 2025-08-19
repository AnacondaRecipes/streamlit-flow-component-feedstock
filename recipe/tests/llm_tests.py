import streamlit as st
from streamlit_flow import StreamlitFlowNode, StreamlitFlowEdge, StreamlitFlowState
from types import SimpleNamespace

def test_node_and_edge_creation():
    # Smoke test: check that nodes and edges can be created with expected attributes
    node = StreamlitFlowNode(
        id="n1",
        pos=(100, 200),
        data={"label": "Test Node"},
        node_type="default",
        source_position="right",
        target_position="left"
    )
    edge = StreamlitFlowEdge(
        id="e1",
        source="n1",
        target="n1"
    )
    assert node.id == "n1"
    assert node.position["x"] == 100
    assert node.position["y"] == 200
    assert edge.id == "e1"
    assert edge.source == "n1"
    assert edge.target == "n1"

def test_state_initialization_empty():
    # Test initialization of an empty state
    state = StreamlitFlowState(nodes=[], edges=[])
    assert state.nodes == []
    assert state.edges == []

def test_streamlit_flow_returns_state():
    # Smoke test: ensure StreamlitFlowState is returned correctly
    nodes = [StreamlitFlowNode(id="n1", pos=(0, 0), data={})]
    edges = [StreamlitFlowEdge(id="e1", source="n1", target="n1")]
    state = StreamlitFlowState(nodes, edges)
    assert state.nodes == nodes
    assert state.edges == edges

def test_session_state_integration(monkeypatch):
    # Smoke test: ensure a new flow state can be stored in Streamlit's session_state
    fake_session = SimpleNamespace()
    monkeypatch.setattr(st, "session_state", fake_session)
    
    nodes, edges = [], []
    if not hasattr(st.session_state, "flow_state"):
        st.session_state.flow_state = StreamlitFlowState(nodes, edges)

    assert isinstance(st.session_state.flow_state, StreamlitFlowState)
    assert st.session_state.flow_state.nodes == []
    assert st.session_state.flow_state.edges == []
