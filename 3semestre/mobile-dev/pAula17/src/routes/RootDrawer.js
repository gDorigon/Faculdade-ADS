import { createDrawerNavigator } from "@react-navigation/drawer";

const Drawer = createDrawerNavigator();

import MainTabs from "./MainTabs";
import TelaSobre from "../pages/TelaSobre";
import { Ionicons } from "@expo/vector-icons";
import cores from "../theme/colors";

export default function RootDrawer() {
  return (
    <Drawer.Navigator
      id="RootDrawer"
      screenOptions={{
        headerStyle: {
          backgroundColor: cores.laranja,
        },
        headerTintColor: cores.branco,
        headerTitleStyle: {
          fontWeight: "bold",
        },
        drawerActiveTintColor: cores.laranja,
      }}
    >
      <Drawer.Screen
        name="MainTabs"
        component={MainTabs}
        options={{
          title: "Sabor Caseiro",
          drawerIcon: ({ size, color }) => (
            <>
              <Ionicons name="home" size={size} color={color} />
            </>
          ),
        }}
      />
      <Drawer.Screen
        name="TelaSobre"
        component={TelaSobre}
        options={{
          title: "Sobre",
          drawerIcon: ({ size, color }) => (
            <>
              <Ionicons name="information-circle" size={size} color={color} />
            </>
          ),
        }}
      />
    </Drawer.Navigator>
  );
}
