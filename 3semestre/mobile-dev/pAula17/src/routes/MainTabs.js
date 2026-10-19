import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

const Tabs = createBottomTabNavigator();

const ICONES_POR_ABA = {
  ReceitasTab: {
    nome: "book",
  },
  FavoritasTab: {
    nome: "heart",
  },
  PerfilTab: {
    nome: "person",
  },
};

import TelaReceitas from "../pages/TelaReceitas";
import TelaFavoritas from "../pages/TelaFavoritas";
import TelaPerfil from "../pages/TelaPerfil";
import cores from "../theme/colors";
import { Ionicons } from "@expo/vector-icons";

export default function MainTabs() {
  return (
    <Tabs.Navigator
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: cores.laranja,
        tabBarStyle: {
          height: 65,
        },
      }}
    >
      <Tabs.Screen
        name="ReceitasTab"
        component={TelaReceitas}
        options={{
          title: "Receitas",
        }}
      />
      <Tabs.Screen
        name="FavoritasTab"
        component={TelaFavoritas}
        options={{
          title: "Favoritas",
        }}
      />
      <Tabs.Screen
        name="PerfilTab"
        component={TelaPerfil}
        options={{
          title: "Perfil",
        }}
      />
    </Tabs.Navigator>
  );
}
