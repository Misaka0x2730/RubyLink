for component in board.GetFootprints():
    component_locked = component.IsLocked()
    if (component_locked):
        component.SetLocked(False)

    component_pos = pcbnew.ToMM(component.GetPosition())
    component_pos = (component_pos[0] - 88.06, 105.87 - component_pos[1])
    component_pos = (round(component_pos[0], 1) + 88.06, 105.87 - round(component_pos[1], 1))
    component.SetPosition(pcbnew.wxPointMM(component_pos[0], component_pos[1]))

    if (component_locked):
        component.SetLocked(True)

pcbnew.Refresh()