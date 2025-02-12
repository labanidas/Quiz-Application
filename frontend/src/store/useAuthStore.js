// src/store/useAuthStore.js
import { defineStore } from "pinia";
import { ref } from "vue";
import { axiosInstance } from "../lib/axios";
import { useToast } from "vue-toast-notification";
import { useRouter } from "vue-router";

export const useAuthStore = defineStore("authStore", () => {
  const router = useRouter();
  const toast = useToast();
  const isSigningUp = ref(false);
  const isLogginIn = ref(false);
  const authUser = ref(null);

  const checkAuth = async () => {
    try {
      const response = await axiosInstance.get("/auth/auth-check");
      authUser.value = response.data.data;
      console.log(response.data.data);
    } catch (error) {
      authUser.value = null;
    }
  };

  const register = async (data) => {
    isSigningUp.value = true;
    try {
      await axiosInstance.post("/auth/register", data);
      toast.success("Please login!", {
        position: "top-right",
        timeout: 3000,
      });
      router.push("/login");
    } catch (error) {
      toast.error(error.message || "Something went wrong!", {
        position: "top-right",
        timeout: 3000,
      });
    } finally {
      isSigningUp.value = false;
    }
  };

  const login = async (data) => {
    isLogginIn.value = true;
    try {
      const response = await axiosInstance.post("/auth/login", data);
      authUser.value = response.data; // update authUser after login
      toast.success("Login successful", {
        position: "top-right",
        timeout: 3000,
      });
      router.push("/dashboard");
    } catch (error) {
      toast.error(error.message || "Something went wrong!", {
        position: "top-right",
        timeout: 3000,
      });
    } finally {
      isLogginIn.value = false;
    }
  };

  const logout = async () => {
    try {
      const response = await axiosInstance.delete("/auth/logout");
      toast.success("Logout successful", {
        position: "top-right",
        timeout: 3000,
      });
      router.push("/login");
    } catch (error) {
      toast.error(error.message || "Something went wrong!", {
        position: "top-right",
        timeout: 3000,
      });
    } finally {
      console.log("logged out");
    }
  };

  return {
    authUser,
    checkAuth,
    isSigningUp,
    isLogginIn,
    register,
    login,
    logout,
  };
});
